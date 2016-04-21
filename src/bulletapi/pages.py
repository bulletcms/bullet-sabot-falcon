from flask import jsonify
from flask.ext.restful import Resource, url_for
from bulletapi.base import bullet_api, bullet_rest_api

mockpageslist = [
    'indexroute',
    'kevin',
    'about'
]

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

@bullet_api.route('/pages', methods=['GET'])
def get_pages():
    return jsonify({'data': mockpageslist})

@bullet_api.route('/pages/<pagename>', methods=['GET'])
def get_page(pagename):
    return jsonify({'data': mockpages[pagename]})
