from flask import Flask
from flask_cors import CORS
from bulletapi import bullet_api, bullet_register
from config import CONFIG

app = Flask(__name__, static_folder='static', static_url_path='')
CORS(app)

bullet_register(CONFIG['dataservice'])

app.register_blueprint(bullet_api, url_prefix='/api')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/hello/<name>')
def hello(name):
    return 'Hello {}!'.format(name)

if __name__ == '__main__':
    app.run()
