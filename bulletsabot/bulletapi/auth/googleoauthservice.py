from oauth2client import client
from .authservice import AuthService

class MockAuthService(AuthService):
    def __init__(self, client_secrets):
        '''
        :param client_secrets: path to client_secret.json
        '''
        self._client_secrets = client_secrets

    def verify(self, auth_code):
        '''
        :param auth_code: authorization code from client
        :return: credentials
        '''
        return client.credentials_from_clientsecrets_and_code(
            self._client_secrets,
            ['profile', 'email'],
            auth_code)

    def login(self, auth_code):
        '''
        :param auth_code: authorization code from client
        '''
        credentials = self.verify(auth_code)
        userid = credentials.id_token['sub']
        email = credentials.id_token['email']
        name = credentials.id_token['name']
        primary_name = credentials.id_token['given_name']

    def logout():
        pass

    def store_credentials():
        pass
