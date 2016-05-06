##########################################
##    Falcon Module                     ##
##########################################

class FalconApiModule:
    def __init__(self, name, configuration={}):
        '''
        :param name: str
        :param configuration: dictionary
        '''
        self._name = name
        self._routes = []
        self._configuration = configuration

    @property
    def name(self):
        return self._name

    def configuration(self, config_key):
        return self._configuration[config_key]

    def add_route(self, uri, resource):
        '''
        :param uri: str
        :param resource: falcon resource object
        '''
        self._routes.append((uri, resource))

    def register(self, api, url_prefix=''):
        '''
        :param api: falcon api object
        '''
        for uri, resource in self._routes:
            api.add_route('{0}{1}'.format(url_prefix, uri), resource)


class FalconApiResource:
    def __init__(self):
        self._resources = []

    def add_resource(self, path, resource, dependencies=[]):
        self._resources.append((path, resource, dependencies))

    def register(self, api):
        for path, resource, dependencies in self._resources:
            api.add_route(path, resource())

class Dependency:
    def __init__(self, key):
        self._key = key

    def inject(self, service):
        self._service = service

    @property
    def service(self):
        return self._service
