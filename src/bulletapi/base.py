from flask import Blueprint
from flask.ext.restful import Api

bullet_api = Blueprint('bulletapi', __name__)
bullet_rest_api = Api(bullet_api)
