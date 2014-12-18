from simpleapi import api_handler, SimpleHttpException


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
def resp_test3(request):

    blah = 1 / 0

    return {
        'value': True
    }
