from .dataservice import DataService

mockpages = {
    'kevin': {
        'title': 'Kevin',
        'tags': [],
        'content': [
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
        ]
    },
    'about': {
        'title': 'About',
        'tags': [],
        'content': [
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
        ]
    },
    'indexroute': {
        'title': 'Home',
        'tags': [],
        'content': [
            {
                'component': 'h1',
                'children': 'Home'
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
}


class MockService(DataService):
    def update_page(self, path, title=None, tags=None, content=None):
        if title is not None:
            mockpages[path]['title'] = title
        if tags is not None:
            mockpages[path]['tags'] = tags
        if content is not None:
            mockpages[path]['content'] = content

    def remove_page(self, path):
        del mockpages[path]

    def get_page(self, path):
        return mockpages[path]

    def has_page(self, path):
        return path in self.get_pagelist()

    def add_page(self, path, title, tags, content):
        mockpages[path] = {
            'title': title,
            'tags': tags,
            'content': content
        }

    def get_pagelist(self):
        return mockpages.keys()

    def change_page_path(self, old_path, new_path):
        page = self.get_page(old_path)
        self.add_page(new_path, page['title'], page['tags'], page['content'])
        self.remove_page(old_path)
