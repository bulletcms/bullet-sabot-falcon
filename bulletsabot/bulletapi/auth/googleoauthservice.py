from oauth2client import client, crypt
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
        try:
            idinfo = client.verify_id_token(id_token, self._client_id)
            # If multiple clients access the backend server:
            if idinfo['aud'] not in self._client_ids:
                raise crypt.AppIdentityError("Unrecognized client.")
            if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                raise crypt.AppIdentityError("Wrong issuer.")
        except crypt.AppIdentityError:
            return (False, None)
        return (True, idinfo)

    def get_userinfo(self, idinfo):
        userinfo = {}

        userinfo['userid'] = idinfo['sub']
        userinfo['email'] = idinfo['email']
        userinfo['name'] = idinfo['name']
        userinfo['primary_name'] = idinfo['given_name']

        return userinfo
