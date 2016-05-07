from gunicorn.app.base import BaseApplication
from gunicorn.six import iteritems
from meinheld.gmeinheld import MeinheldWorker
from app import app as application
from config import CONFIG

MeinheldWorker

class Capsule(BaseApplication):
    def __init__(self, app, options={}):
        self.options = options
        self.application = app
        super(Capsule, self).__init__()

    def load_config(self):
        config = dict([(key, value) for key, value in iteritems(self.options)
                       if key in self.cfg.settings and value is not None])
        for key, value in iteritems(config):
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


if __name__ == '__main__':
    cfg = CONFIG['gunicorn']
    Capsule(application, options={
        'bind': '{}:{}'.format(cfg['host'], cfg['port']),
        'workers': cfg['workers'],
        'worker-class': '.capsule.MeinheldWorker'
    }).run()
