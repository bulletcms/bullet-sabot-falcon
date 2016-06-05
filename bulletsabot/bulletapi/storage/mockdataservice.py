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
                'children': 'Hi, I am Kevin'
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
                'children': 'BulletAPI is a minimal and configural system for content management.'
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
        'title': 'BulletAPI',
        'tags': [],
        'content': [
            {
                'component': 'h1',
                'children': 'BulletAPI'
            },
            {
                'component': 'p',
                'children': 'Hello World!'
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

mockusers = {
    'kevin': {
        'public': {
            'username': 'kevin'
        },
        'private': {
            'passhash': ';akldjsf;laksjdf',
            'email': 'example@example.com',
            'googleoauthcode': 'a;slkdfja;slkdjf'
        }
    }
}


class MockDataService(DataService):
    def add_user(self, user_id, public_props, private_props):
        user = {
            'public': {},
            'private': {}
        }
        for key, value in public_props.items():
            if key in self.userprops_public:
                user['public'][key] = value
        for key, value in private_props.items():
            if key in self.userprops_private:
                user['private'][key] = value

        mockusers[user_id] = user

    def remove_user(self, user_id):
        del mockusers[user_id]

    def update_user(self, user_id, public_props, private_props):
        user = {}
        for key, value in public_props.items():
            if key in self.userprops_public:
                user['public'][key] = value
        for key, value in private_props.items():
            if key in self.userprops_private:
                user['private'][key] = value

        mockusers[user_id] = {**mockusers[user_id], **user}

    def has_user(self, user_id):
        return user_id is not None and user_id in mockusers

    def get_user_public(self, user_id):
        return mockusers[user_id]['public']

    def get_user(self, user_id):
        return {**mockusers[user_id]['public'], **mockusers[user_id]['private']}



    def update_page(self, path, props):
        page = {}

        for key, value in props.items():
            if key in self.pageprops:
                page[key] = value

        mockpages[path] = {**mockpages[path], **page}

    def remove_page(self, path):
        del mockpages[path]

    def get_page(self, path):
        return mockpages[path]

    def has_page(self, path):
        return path in self.get_pagelist()

    def add_page(self, path, props):
        page = {}

        for key, value in props.items():
            if key in self.pageprops:
                page[key] = value

        mockpages[path] = page

    def get_pagelist(self):
        return list(mockpages.keys())

    def change_page_path(self, old_path, new_path):
        page = self.get_page(old_path)
        self.add_page(new_path, page['title'], page['tags'], page['content'])
        self.remove_page(old_path)
