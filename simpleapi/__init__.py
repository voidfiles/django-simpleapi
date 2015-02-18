import logging
import json
import sys

from corsheaders.middleware import CorsMiddleware
from django.http import HttpResponse, Http404
from django.conf import settings
from django.conf.urls import patterns, url
from django.core.urlresolvers import RegexURLResolver
from django.views.decorators.csrf import csrf_exempt

from .utils import CaseInsensitiveDict

logger = logging.getLogger(__name__)

__all__ = ('SimpleHttpException', 'api_handler', 'api_export')
__version__ = '1.4.0'

cors_middleware = None

if getattr(settings, 'SIMPLEAPI_ENABLE_CORS', False):
    cors_middleware = CorsMiddleware()


def allow_cors(func):
    def func_wrapper(request, *args, **kwargs):
        resp = cors_middleware.process_request(request)
        if not resp:
            resp = func(request, *args, **kwargs)

        resp = cors_middleware.process_response(request, resp)

        return resp

    return func_wrapper


class SimpleHttpException(Exception):
    def __init__(self, message, error_slug, code=400, info=None):
        super(SimpleHttpException, self).__init__(message)
        self.code = code
        self.error_slug = error_slug
        self.info = info


def create_exception_response(request, error_message, error_slug, code, info):
    request.META['_simple_api_meta']['code'] = code
    request.META['_simple_api_meta']['error_message'] = error_message
    request.META['_simple_api_meta']['error_slug'] = error_slug
    request.META['_simple_api_meta']['error_info'] = info

    return code


def get_meta(request, code):
    meta = request.META.get('_simple_api_meta', dict())
    meta['code'] = code

    return meta


def api_handler(func):
    def inner(request, *args, **kwargs):
        request.META['_simple_api_meta'] = request.META.get('_simple_api_meta', dict())
        data = None
        code = 200

        try:
            data = func(request, *args, **kwargs)
        except SimpleHttpException:
            e = sys.exc_info()[1]
            code = create_exception_response(request, e.message, e.error_slug, e.code, e.info)
            data = None
        except Exception:
            logger.exception('caught an unhandled exception in %s', func)
            code = create_exception_response(request, 'Unhandled Exception', 'unhandled', 500, None)
            data = None

        resp_envelope = {
            'meta': get_meta(request, code)
        }

        if data is not None:
            resp_envelope['data'] = data

        pp = request.META.get('HTTP_X_PRETTY_PRINT_JSON', '0') == '1'
        if pp:
            content = json.dumps(resp_envelope, sort_keys=True, indent=4)
        else:
            content = json.dumps(resp_envelope)

        return HttpResponse(content, content_type='application/json', status=code)

    return inner


url_patterns = CaseInsensitiveDict()
resolvers = CaseInsensitiveDict()


def api_export(method, path):
    def _inner(func):
        url_pattern = url_patterns.get(method)
        if not url_pattern:
            url_pattern = url_patterns[method] = patterns('')

        resolver = resolvers.get(method)
        if not resolver:
            resolver = resolvers[method] = RegexURLResolver('', url_pattern)

        full_path = path + r'/?$'

        func = api_handler(func)

        url_pattern += patterns('', url(full_path, func, name=func.__name__))

        return func

    return _inner


def api_export_handler(request, path):
    resolver = resolvers.get(request.method)
    if not resolver:
        raise Http404()

    view_func, view_args, view_kwargs = resolver.resolve(path)

    return view_func(request, *view_args, **view_kwargs)

if cors_middleware:
    api_export_handler = allow_cors(api_export_handler)

if getattr(settings, 'SIMPLEAPI_ENABLE_CSRF', False) is False:
    api_export_handler = csrf_exempt(api_export_handler)

simple_api_patterns = patterns(
    '',
    url(r'^(?P<path>.+)$', api_export_handler),
)
