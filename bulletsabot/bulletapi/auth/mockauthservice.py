from oauth2client import client
from .authservice import AuthService

class MockAuthService(AuthService):
    def __init__(self, client_secrets, redirect_uri):
        self._client_secrets = client_secrets
        self._redirect_uri = redirect_uri

    def login(self):
        flow = client.flow_from_clientsecrets(
            self._client_secrets,
            scope='https://www.googleapis.com/auth/drive.metadata.readonly',
            redirect_uri=self._redirect_uri,
            include_granted_scopes=True)

    def logout():
        pass

    def credentials():
        pass
