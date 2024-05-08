from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import DirectorManager
from registrations.models import CustomUser


class Director(CustomUser):

    objects = DirectorManager()

    class Meta:
        proxy = True
        verbose_name = _("réalisateur")
        verbose_name_plural = _("réalisateurs")
