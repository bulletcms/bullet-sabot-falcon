from falcon import API
from bulletapi import bullet_api
from bulletapi.storage import MockDataService

app = API()

bullet_api\
    .inject('data_service', MockDataService())\
    .build()\
    .register(app, url_prefix='/api')
