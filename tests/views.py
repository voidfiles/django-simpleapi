from simpleapi import api_handler, api_export, SimpleHttpException


@api_handler
def resp_test(request):
    return {
        'value': True
    }


@api_handler
def resp_test2(request):

    raise SimpleHttpException("Missing data", 'missing-data', 400)

    return {
        'value': True
    }

@api_handler
def empty_response_test(request):
    return []

@api_handler
def resp_test3(request):

    blah = 1 / 0

    return {
        'value': True
    }


@api_export(method='GET', path=r'test1')
def resp_export_test1(request):
    return {
        'value': True
    }

@api_export(method='GET', path=r'test2/(?P<param>[0-9]+)')
def resp_export_test1(request, param):
    return {
        'value': param
    }

