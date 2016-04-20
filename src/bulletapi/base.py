from flask import Blueprint
from flask.ext.restful import Api

bulletapi = Blueprint('bulletapi', __name__)
bulletrestapi = Api(bulletapi)
