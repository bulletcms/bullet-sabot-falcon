from .base import bullet_rest_api
from .pages import PageResource

def bullet_register(dataservice):
    '''
    :param dataservice: dataservice object
    :return:
    '''
    PageResource(bullet_rest_api, dataservice).register()
