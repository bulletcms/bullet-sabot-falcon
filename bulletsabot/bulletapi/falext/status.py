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
        import falcon
        HTTPSTATUS[code] = getattr(falcon, 'HTTP_{0}'.format(code))
        return HTTPSTATUS[code]
