from .module import Fmod

from .pages import PageContainer
from .users import UserContainer

MAGIC_DATA_SERVICE = 'data_service'

bullet_api = Fmod.Module('bullet_api', [MAGIC_DATA_SERVICE])

PageContainer(bullet_api)
UserContainer(bullet_api)
