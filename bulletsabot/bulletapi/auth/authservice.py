class AuthService:
    def verify():
        '''
        verifies given code
        '''
        raise NotADirectoryError("Not implemented")

    def login():
        '''
        gets credentials from service and stores in cache
        '''
        raise NotImplementedError("Not implemented")

    def logout(user_id):
        '''
        invalidates credentials
        :param user_id: id of user session
        '''
        raise NotImplementedError("Not implemented")

    def store_credentials(user_id):
        '''
        stores credentials to cache
        :param user_id: id of user session
        '''
        raise NotImplementedError("Not implemented")
