class DataService:

    # PAGE TRANSACTIONS
    def add_page(self, path, title, tags, content):
        raise NotImplementedError("Not implemented")

    def update_page(self, path, title=None, tags=None, content=None):
        raise NotImplementedError("Not implemented")

    def remove_page(self, path):
        raise NotImplementedError("Not implemented")

    def change_page_path(self, old_path, new_path):
        raise NotImplementedError("Not implemented")

    # PAGE QUERIES
    def get_page(self, path):
        raise NotImplementedError("Not implemented")

    def get_pagelist(self):
        raise NotImplementedError("Not implemented")

    def has_page(self, path):
        raise NotImplementedError("Not implemented")
