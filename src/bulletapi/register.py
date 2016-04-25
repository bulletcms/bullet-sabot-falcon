from .base import bullet_rest_api
from .pages import PageResource
from .storage import GCDService, MockService

def bullet_register(dataservice, gcd_project_id=None):
    '''
    :param dataservice: string
    :param gcd_project_id: optional - required only if dataservice is google-cloud-datastore
    :return:
    '''
    service = None
    if dataservice == 'google-cloud-datastore':
        service = GCDService(gcd_project_id)
    elif dataservice == 'mock-database':
        service = MockService()
    else:
        raise ValueError("{} is not a valid dataservice string".format(dataservice))
    PageResource(bullet_rest_api, service).register()
