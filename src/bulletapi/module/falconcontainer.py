##########################################
##    Falcon Container                  ##
##########################################

class Container:
    def inject(self, key, service):
        self._dependencies[key].inject(service)

    def instantiate(self, configuration):
        '''
        :return: resources: list of tuples(path: str, resource: Falcon Resource objects)
        '''
        raise NotImplementedError("Not implemented")

    def register(self, api):
        resources = self.instantiate(api.)
        for path, resource in resources:
            api.add_route(path, resource)
