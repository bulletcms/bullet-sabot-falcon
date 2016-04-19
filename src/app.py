from flask import Flask
from flask.ext.cors import CORS
from bulletapi import bulletapi

app = Flask(__name__, static_folder='static', static_url_path='')
CORS(app)

app.register_blueprint(bulletapi, url_prefix='/api')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/hello/<name>')
def hello(name):
    return 'Hello {}!'.format(name)

if __name__ == '__main__':
    app.run()
