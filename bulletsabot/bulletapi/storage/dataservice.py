##########################################
##    Base Data Service                 ##
##########################################

class DataService:

    # USERS
    userprops_public = set(['username'])
    userprops_private = set(['email', 'googleoauthcode'])

    def add_user(self, user_id, passwd, public_props, private_props):
        raise NotImplementedError("Not implemented")

    def remove_user(self, user_id):
        raise NotImplementedError("Not implemented")

    def update_user(self, user_id, public_props, private_props):
        raise NotImplementedError("Not implemented")

    def has_user(self, user_id):
        raise NotImplementedError("Not implemented")

    def get_user_public(self, user_id):
        raise NotImplementedError("Not implemented")

    def get_user(self, user_id):
        raise NotImplementedError("Not implemented")

    # PAGE TRANSACTIONS
    pageprops = set(['title', 'tags', 'content'])

    def add_page(self, path, title, tags, content):
        raise NotImplementedError("Not implemented")

    def update_page(self, path, dictionary):
        '''
        dictionary: title, tags, content
        '''
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
