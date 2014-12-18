import logging
import json
import sys

from django.http import HttpResponse

logger = logging.getLogger(__name__)

__all__ = ('SimpleHttpException', 'api_handler')
__version__ = '1.0'


class SimpleHttpException(Exception):
    def __init__(self, message, error_slug, code=400):
        super(SimpleHttpException, self).__init__(message)
        self.code = code
        self.error_slug = error_slug


def create_exception_response(request, error_message, error_slug, code):
    request.META['_simple_api_meta']['code'] = code
    request.META['_simple_api_meta']['error_message'] = error_message
    request.META['_simple_api_meta']['error_slug'] = error_slug

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
            code = create_exception_response(request, e.message, e.error_slug, e.code)
        except Exception:
            logger.exception('caught an unhandled exception in %s', func)
            code = create_exception_response(request, 'Unhandled Exception', 'unhandled', 500)

        resp_envelope = {
            'meta': get_meta(request, code)
        }

        if data:
            resp_envelope['data'] = data

        pp = request.META.get('HTTP_X_PRETTY_PRINT_JSON', '0') == '1'
        if pp:
            content = json.dumps(resp_envelope, sort_keys=True, indent=4)
        else:
            content = json.dumps(resp_envelope)

        return HttpResponse(content, content_type='application/json', status=code)

    return inner
