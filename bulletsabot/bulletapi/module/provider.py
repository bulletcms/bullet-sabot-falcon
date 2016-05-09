from .dependency import Dependency

##########################################
##    Provider                          ##
##########################################

class Provider:
    def __init__(self, dependency_keys):
        '''
        :param dependency_keys: list[str]
        '''
        self._dependencies = {}
        for key in dependency_keys:
            self._dependencies[key] = Dependency(key)

    @property
    def keys(self):
        return list(self._dependencies.keys())

    def inject(self, key, service):
        '''
        injects service into dependency of key
        :param key: str
        :param service: dependency service object
        '''
        if key not in self._dependencies:
            raise KeyError("key {} is not a dependency".format(key))
        self._dependencies[key].inject(service)

    def provide(self, key):
        '''
        :return: dependency of key
        '''
        return self._dependencies[key]
