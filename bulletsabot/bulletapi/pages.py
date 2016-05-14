import ujson
from falcon import HTTPNotFound, HTTPBadRequest, before
from falext import httpstatus
from .module import Fmod


##########################################
##    Pages API                         ##
##########################################

def abort_if_page_dne(req, resp, resource, params):
    if not resource._data_service.has_page(params['page_id']):
        raise HTTPNotFound()


# PAGE COLLECTION RESOURCE
class PagesCollection:
    def __init__(self, data_service):
        self._data_service = data_service

    def on_get(self, req, res):
        res.status = httpstatus(200)
        res.body = ujson.dumps({'data': self._data_service.get_pagelist()})


# PAGE RESOURCE
class Page:
    def __init__(self, data_service):
        self._data_service = data_service

    @before(abort_if_page_dne)
    def on_get(self, req, res, page_id):
        res.status = httpstatus(200)
        res.body = ujson.dumps({'data': self._data_service.get_page(page_id)})

    @before(abort_if_page_dne)
    def on_delete(self, req, res, page_id):
        self._data_service.remove_page(page_id)
        res.status = httpstatus(204)
        res.body = ujson.dumps({'data': 'deleted page {}'.format(page_id)})

    def on_post(self, req, res, page_id):
        try:
            raw_json = req.stream.read()
        except Exception as ex:
            raise HTTPBadRequest('Error', ex.message)

        try:
            data = ujson.loads(raw_json, encoding='utf-8')['data']
            self._data_service.add_page(page_id, data['title'], data['tags'], data['content'])
            res.status = httpstatus(201)
            res.body = ujson.dumps({'data': 'posted page {}'.format(page_id)})
        except ValueError:
            raise HTTPBadRequest('Invalid JSON', 'Could not decode the request body')

    @before(abort_if_page_dne)
    def put(self, req, res, page_id):
        try:
            raw_json = req.stream.read()
        except Exception as ex:
            raise HTTPBadRequest('Error', ex.message)

        try:
            data = ujson.loads(raw_json, encoding='utf-8')['data']
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
            res.status = httpstatus(201)
            res.body = ujson.dumps({'data': 'put page {}'.format(page_id)})
        except ValueError:
            raise HTTPBadRequest('Invalid JSON', 'Could not decode the request body.')


MAGIC_DATA_SERVICE = 'data_service'

class PageContainer(Fmod.Container):
    def initialize(self, provider):
        self._data_dependency = provider.provide(MAGIC_DATA_SERVICE)

    def config(self):
        return [
            ('/pages', PagesCollection(self._data_dependency.service)),
            ('/pages/{page_id}', Page(self._data_dependency.service))
        ]
