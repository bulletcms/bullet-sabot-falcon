from .falconapimodule import FalconApiModule

from .pages import PagesResource

def bullet_api():
    FalconApiModule('bullet_api')

PagesResource().register(bullet_api)
