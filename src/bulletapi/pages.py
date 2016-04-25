from flask.ext.restful import Resource, reqparse, abort

##########################################
##    Restful                           ##
##########################################

def abort_if_page_dne(func):
    def decorated_func(self, page_id):
        if not self._data_service.has_page(page_id):
            abort(404, message='Page {} does not exist'.format(page_id))
        return func(page_id)
    return decorated_func


class PageResource:
    def __init__(self, api, data_service):
        self._api = api
        self._data_service = data_service
        # REQUEST PARSER
        self._argparser = reqparse.RequestParser()
        self._argparser.add_argument('data', required=True)

    def register(self):

        class Pages(Resource):
            _data_service = self._data_service
            _argparser = self._argparser

            def get(self):
                return {'data': self._data_service.get_pagelist()}


        class Page(Resource):
            _data_service = self._data_service
            _argparser = self._argparser

            @abort_if_page_dne
            def get(self, page_id):
                return {'data': self._data_service.get_page(page_id)}

            @abort_if_page_dne
            def delete(self, page_id):
                self._data_service.remove_page(page_id)
                return ('', 204)

            def post(self, page_id):
                data = self._argparser.parse_args()['data']
                self._data_service.add_page(page_id, data['title'], data['tags'], data['content'])
                return '', 201

            @abort_if_page_dne
            def put(self, page_id):
                data = self._argparser.parse_args(strict=True)['data']
                title = None
                tags = None
                content = None
                if 'title' in data:
                    title = data['title']
                if 'tags' in data:
                    tags = data['tags']
                if 'content' in data:
                    content = data['content']
                self._data_service.update_page(page_id, title, tags, content)
                return ('', 201)


        self._api.add_resource(Pages, '/pages')
        self._api.add_resource(Page, '/pages/<page_id>')
