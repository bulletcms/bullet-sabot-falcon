from gcloud import datastore
from .dataservice import DataService

##########################################
##    Google Datastore Configuration    ##
##########################################


##########################################
##    Google Datastore Service          ##
##########################################

class GCDService(DataService):

    def __init__(self, project_id):
        self._project_id = project_id
        self._client = datastore.Client()


    @property
    def project_id(self):
        return self._project_id


    # PAGE TRANSACTIONS
    def add_page(self, path, title, tags, content):
        page = datastore.Entity(
            self._client.key('Pagelist', 'main', 'Page', path),
            exclude_from_indexes=['title', 'content']
        )
        page.update({
            'path': path,
            'tags': tags,
            'title': title,
            'content': content
        })
        self._client.put(page)


    def update_page(self, path, title=None, tags=None, content=None):
        with self._client.transaction():
            page = self._client.get(self._client.key('Pagelist', 'main', 'Page', path))

            if title is not None:
                page['title'] = title

            if tags is not None:
                page['tags'] = tags

            if content is not None:
                page['content'] = content

            self._client.put(page)

    def remove_page(self, path):
        self._client.delete(self._client.key('Pagelist', 'main', 'Page', path))

    def change_page_path(self, old_path, new_path):
        with self._client.transaction():
            page = self._client.get(self._client.key('Pagelist', 'main', 'Page', old_path))

            self.add_page(new_path, page['title'], page['tags'], page['content'])
            self.remove_page(old_path)


    # PAGE QUERIES
    def get_page(self, path):
        return self._client.get(self._client.key('Pagelist', 'main', 'Page', path))

    def get_pagelist(self):
        query = self._client.query(kind='Page', ancestor=self._client.key('Pagelist', 'main'))
        query.keys_only()
        return list(query.fetch())

    def has_page(self, path):
        return path in self.get_pagelist()
