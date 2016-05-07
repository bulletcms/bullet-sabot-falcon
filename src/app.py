from falcon import API
from bulletapi import bullet_api, DataServices

app = API()

bullet_api\
    .inject('data_service', DataServices.MockService())\
    .build()\
    .register(app, url_prefix='/api')
