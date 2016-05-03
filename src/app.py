from flask import Flask
from flask_cors import CORS
from bulletapi import bullet_api, bullet_register, Services

sabotapp = Flask(__name__, static_folder='static', static_url_path='')
CORS(sabotapp)

bullet_register(Services.MockService())

sabotapp.register_blueprint(bullet_api, url_prefix='/api')

@sabotapp.route('/')
def index():
    return sabotapp.send_static_file('index.html')

@sabotapp.route('/hello/<name>')
def hello(name):
    return 'Hello {}!'.format(name)

if __name__ == '__main__':
    sabotapp.run(host='0.0.0.0', port=5000, debug=None)
