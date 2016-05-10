from .capsule import Capsule
from .app import app as application
from .config import CONFIG

Capsule(application, options=CONFIG['gunicorn']).run()
