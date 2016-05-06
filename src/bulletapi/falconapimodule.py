##########################################
##    Falcon Module                     ##
##########################################

class FalconModule:
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


class FalconComponent:
    def __init__(self):
        self._dependencies = {}

    def inject(self, key, service):
        self._dependencies[key].inject(service)

    def instantiate(self):
        '''
        :return: tuple(resources: list of tuples(path: str, resource: Falcon Resource objects), dependencies: Dependency objects)
        '''
        raise NotImplementedError("Not implemented")

    def register(self, api):
        resources, dependencies = self.instantiate()
        for path, resource in resources:
            api.add_route(path, resource())

class Dependency:
    def __init__(self, key):
        self._key = key
        self._service = None

    def inject(self, service):
        self._service = service

    @property
    def service(self):
        if self._service is None:
            raise RuntimeError("Service not injected")
        return self._service
