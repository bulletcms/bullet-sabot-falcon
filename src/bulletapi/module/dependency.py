##########################################
##    Dependency                        ##
##########################################

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
