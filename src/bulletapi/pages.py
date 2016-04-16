from flask import jsonify
from base import bulletapi

mockpageslist = [
    'indexroute',
    'kevin'
]

mockpages = {
    'kevin': [
        {
            'component': 'h1',
            'children': 'Kevin'
        },
        {
            'component': 'p',
            'children': 'this is just a test page'
        },
        {
            'component': 'DateView',
            'config': {
                'date': 1460146245,
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
