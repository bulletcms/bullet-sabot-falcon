import ujson
from falcon import HTTPNotFound, HTTPBadRequest, before
from .falext import httpstatus
from .module import Fmod

def abort_if_user_dne(req, resp, resource, params):
    if not resource._data_service.has_user(params['user_id']):
        raise HTTPNotFound()

def abort_if_user_exists(req, resp, resource, params):
    if resource._data_service.has_user(params['user_id']):
        raise HTTPBadRequest()

class User:
    def __init__(self, data_service):
        self._data_service = data_service

    @before(abort_if_user_dne)
    def on_get(self, req, res, user_id):
        res.status = httpstatus(200)
        res.body = ujson.dumps({'data': self._data_service.get_user_public(user_id)})

    @before(abort_if_user_dne)
    def on_delete(self, req, res, user_id):
        self._data_service.remove_user(user_id)
        res.status = httpstatus(204)
        res.body = ujson.dumps({'data': 'deleted user {}'.format(user_id)})

    @before(abort_if_user_exists)
    def on_post(self, req, res, user_id):
        try:
            raw_json = req.stream.read()
        except Exception as ex:
            raise HTTPBadRequest('Error', ex.message)

        try:
            data = ujson.loads(raw_json)['data']
            self._data_service.add_user(user_id, data['public'], data['private'])
            res.status = httpstatus(201)
            res.body = ujson.dumps({'data': 'added user {}'.format(user_id)})
        except ValueError:
            raise HTTPBadRequest('Invalid JSON', 'Could not decode the request body')

    @before(abort_if_user_dne)
    def put(self, req, res, user_id):
        try:
            raw_json = req.stream.read()
        except Exception as ex:
            raise HTTPBadRequest('Error', ex.message)

        try:
            data = ujson.loads(raw_json)['data']
            self._data_service.update_user(user_id, data)
            res.status = httpstatus(201)
            res.body = ujson.dumps({'data': 'udpated user {}'.format(user_id)})
        except ValueError:
            raise HTTPBadRequest('Invalid JSON', 'Could not decode the request body.')


MAGIC_DATA_SERVICE = 'data_service'

class UserContainer(Fmod.Container):
    def initialize(self, provider):
        self._data_dependency = provider.provide(MAGIC_DATA_SERVICE)

    def config(self):
        return [
            ('/users/{user_id}', User(self._data_dependency.service))
        ]
