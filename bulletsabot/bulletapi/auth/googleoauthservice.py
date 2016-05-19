from oauth2client import client
from .authservice import AuthService

class MockAuthService(AuthService):
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

    def login(self, auth_code):
        '''
        :param auth_code: authorization code from client
        '''
        valid, idinfo = self.verify(auth_code)
        if not valid:
            pass
        else:
            userid = idinfo['sub']
            email = idinfo['email']
            name = idinfo['name']
            primary_name = idinfo['given_name']

    def logout():
        pass
