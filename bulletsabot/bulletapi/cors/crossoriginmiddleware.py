class CorsMiddleware:
    def __init__(self, allowed_origins):
        '''
        :param allowed_origins: list of origin urls
        '''
        self._allowed_origins = allowed_origins

    def process_request(self, request, response):
        origin = request.get_header('Origin')
        if origin in self._allowed_origins:
            response.set_header('Access-Control-Allow-Origin', origin)
