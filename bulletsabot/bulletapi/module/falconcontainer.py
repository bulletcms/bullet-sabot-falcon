##########################################
##    Falcon Container                  ##
##########################################

class Container:
    def __init__(self, module):
        '''
        adds self to the module and initializes dependencies
        :param module: Falcon Module object
        '''
        self.initialize(module.provider)
        module.add_container(self)

    def initialize(self, provider):
        '''
        initialize local dependencies
        :param provider: api dependency provider
        '''
        raise NotImplementedError("Not implemented")

    def config(self):
        '''
        :return: list of resource tuples(path: str, resource: Falcon Resource objects)
        '''
        raise NotImplementedError("Not implemented")

    def register(self, module):
        '''
        :param module: Falcon Module object
        '''
        for path, resource in self.config():
            module.add_route(path, resource)
