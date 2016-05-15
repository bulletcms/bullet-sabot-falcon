from importlib import import_module

STATUSES = set([200, 201, 204, 400])

HTTPSTATUS = {}

def httpstatus(code):
    '''
    :param code: 3 digit html status code
    '''
    assert isinstance(code, int) and code > 99 and code < 1000

    if code in HTTPSTATUS:
        return HTTPSTATUS[code]
    elif code in STATUSES:
        HTTPSTATUS[code] = import_module('falcon.HTTP_{0}'.format(code))
        return HTTPSTATUS[code]
