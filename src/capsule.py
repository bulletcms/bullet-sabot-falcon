from gunicorn.app.base import BaseApplication
from gunicorn.six import iteritems
from app import app as application
from config import CONFIG

from meinheld.gmeinheld import MeinheldWorker

WORKERS = {
    'meinheld': 'capsule.MeinheldWorker'
}

def options(cfg):
    if 'worker_class' in cfg:
        # only import workers if necessary
        if cfg['worker_class'] == 'meinheld':
            pass

    return {
        'bind': '{0}:{1}'.format(cfg['host'], cfg['port']) or '0.0.0.0:8080',
        'workers': cfg['workers'] or 1,
        'worker_class': WORKERS[cfg['worker_class']] or cfg['worker_class'] or 'sync'
    }

class Capsule(BaseApplication):
    def __init__(self, app, options={}):
        self.options = options
        self.application = app
        super(Capsule, self).__init__()

    def load_config(self):
        config = dict([
            (key, value)
            for key, value in iteritems(self.options)
            if key in self.cfg.settings and value is not None])
        for key, value in iteritems(config):
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


if __name__ == '__main__':
    Capsule(application, options=options(CONFIG['gunicorn'])).run()
