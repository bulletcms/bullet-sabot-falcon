from flask.ext.restful import Resource, reqparse, abort
from .base import bullet_rest_api
from .storage import GCDService


##########################################
##    Data                              ##
##########################################
mockpageslist = {
    'indexroute',
    'kevin',
    'about'
}

mockpages = {
    'kevin': [
        {
            'component': 'h1',
            'children': 'Kevin'
        },
        {
            'component': 'p',
            'children': 'hi, i am kevin'
        },
        {
            'component': 'DateView',
            'props': {
                'date': 1460146245,
                'author': 'xorkevin'
            }
        }
    ],
    'about': [
        {
            'component': 'h1',
            'children': 'About'
        },
        {
            'component': 'p',
            'children': 'this is the about page'
        },
        {
            'component': 'DateView',
            'props': {
                'date': 1461113451,
                'author': 'xorkevin'
            }
        }
    ],
    'indexroute': [
        {
            'component': 'h1',
            'children': 'indexroute'
        },
        {
            'component': 'p',
            'children': 'this is just a test home page for the index route'
        },
        {
            'component': 'DateView',
            'props': {
                'date': 1461052472,
                'author': 'xorkevin'
            }
        }
    ]
}


# Google Cloud Datastore Service
# googlecloud = GCDService('bullet-sabot-test')


##########################################
##    Restful                           ##
##########################################

# REQUEST PARSER
reqparser = reqparse.RequestParser()
reqparser.add_argument('data')


# PAGE LIST
def abort_if_page_exists(page_id):
    if page_id in mockpageslist:
        abort(409, message='Page {} already exists'.format(page_id))

class Pages(Resource):
    def get(self):
        return {'data': list(mockpageslist)}

    def post(self):
        req = reqparser.parse_args().data
        abort_if_page_exists(req.path)
        mockpages[req.path] = req.content
        return '', 201

bullet_rest_api.add_resource(Pages, '/pages')


# PAGES
def abort_if_page_dne(page_id):
    if page_id not in mockpageslist:
        abort(404, message='Page {} does not exist'.format(page_id))

class Page(Resource):
    def get(self, page_id):
        abort_if_page_dne(page_id)
        return {'data': mockpages[page_id]}

    def delete(self, page_id):
        abort_if_page_dne(page_id)
        mockpageslist.remove(page_id)
        del mockpages[page_id]
        return ('', 204)

    def put(self, page_id):
        abort_if_page_dne(page_id)
        mockpages[page_id] = reqparser.parse_args().data.content
        return ('', 201)

bullet_rest_api.add_resource(Page, '/pages/<page_id>')
