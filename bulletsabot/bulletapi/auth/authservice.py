class AuthService:
    def verify(self, id_token):
        '''
        verifies given token
        :param id_token: id_token from client
        :return: tuple(valid, idinfo)
        '''
        raise NotADirectoryError("Not implemented")

    def get_userinfo(idinfo):
        '''
        gets userinfo from idinfo
        :param idinfo: idinfo from verify
        '''
        raise NotImplementedError("Not implemented")
