from falcon import API
from bulletapi import bullet_api
from bulletapi.storage import MockDataService
from bulletapi.cors import CorsMiddleware

app = API(middleware=[CorsMiddleware(['http://localhost:3000', 'http://localhost:5000'])])

bullet_api\
    .inject('data_service', MockDataService())\
    .build()\
    .register(app, url_prefix='/api')
