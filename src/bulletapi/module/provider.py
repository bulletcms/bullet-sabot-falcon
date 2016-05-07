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

    def inject(self, key, service):
        '''
        injects service into dependency of key
        :param key: str
        :param service: dependency service object
        '''
        self._dependencies[key].inject(service)

    def provide(self, key):
        '''
        :return: dependency of key
        '''
        return self._provider[key]
