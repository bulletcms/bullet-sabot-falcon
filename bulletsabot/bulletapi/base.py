from .module import Fmod

from .pages import PageContainer, MAGIC_DATA_SERVICE

bullet_api = Fmod.Module('bullet_api', [MAGIC_DATA_SERVICE])

PageContainer(bullet_api)
