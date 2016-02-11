from django.apps import AppConfig
from django.conf import settings


class UsertemplatesConfig(AppConfig):
    name = 'usertemplates'
    verbose_name = 'User Templates'
    if getattr(settings, 'USERTEMPLATES_TEMPLATES'):
        templates = getattr(settings, 'TEMPLATES')[0]
        templates_dirs = getattr(templates[0], 'DIRS')
