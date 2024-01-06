from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DirectorsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'directors'
    verbose_name = _("réalisateurs")
