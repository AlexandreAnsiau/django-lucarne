from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class RegistrationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'registrations'
    verbose_name = _("utilisateurs")
