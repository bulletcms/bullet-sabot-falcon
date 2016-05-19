from oauth2client import client
from .authservice import AuthService

class GoogleOAuthService(AuthService):
    def __init__(self, client_id, client_ids):
        '''
        :param client_id: client_id of the api
        :param client_ids: list of client ids
            ex: webclient, android client, etc.
        '''
        self._client_id = client_id
        self._client_ids = client_ids

    def verify(self, id_token):
        '''
        :param token: id_token from client
        :return: tuple(token validity - bool, idinfo or error)
        '''
        idinfo = client.verify_id_token(id_token, self._client_id)
        if idinfo['aud'] not in self._client_ids:
            return (False, "Unrecognized client.")
        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            return (False, "Wrong issuer.")
        return (True, idinfo)

    def login(self, id_token):
        '''
        :param id_token: id_token from client
        '''
        valid, idinfo = self.verify(id_token)
        if not valid:
            # attempt to get a new id_token
            pass
        else:

            return idinfo['sub']  # userid

    def logout(self, id_token):
        # invalidate id_token
        pass

    def get_idinfo(self, id_token):
        '''
        :param id_token: id_token from client
        '''
        idinfo = None  # get idinfo using api, not verification

        userinfo = {}

        userinfo['userid'] = idinfo['sub']
        userinfo['email'] = idinfo['email']
        userinfo['name'] = idinfo['name']
        userinfo['primary_name'] = idinfo['given_name']

        return userinfo
