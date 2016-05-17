class AuthService:
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

    def credentials(user_id):
        '''
        gets credentials from cache
        :param user_id: id of user session
        '''
        raise NotImplementedError("Not implemented")
