from flask import jsonify
from base import bulletapi

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

@bulletapi.route('/pages', methods=['GET'])
def get_pages():
    return jsonify({'data': mockpageslist})

@bulletapi.route('/pages/<pagename>', methods=['GET'])
def get_page(pagename):
    return jsonify({'data': mockpages[pagename]})
