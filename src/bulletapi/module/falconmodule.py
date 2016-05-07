from .provider import Provider

##########################################
##    Falcon Module                     ##
##########################################

class Module:
    def __init__(self, name, dependency_keys):
        '''
        :param name: str
        :param provider: dictionary of dependencies
        '''
        self._name = name
        self._routes = []
        self._provider = Provider(dependency_keys)

    @property
    def name(self):
        return self._name

    @property
    def provider(self):
        return self._provider

    def add_route(self, uri, resource):
        '''
        :param uri: str
        :param resource: falcon resource object
        '''
        self._routes.append((uri, resource))

    def register(self, falcon_api, url_prefix=''):
        '''
        :param falcon_api: falcon api object
        '''
        for uri, resource in self._routes:
            falcon_api.add_route('{0}{1}'.format(url_prefix, uri), resource)
