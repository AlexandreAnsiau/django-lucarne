from django.db import models

from .managers import DirectorManager
from registrations.models import CustomUser


class Directors(CustomUser):

    objects = DirectorManager

    class Meta:
        proxy = True
        verbose_name = _("réalisateur")
        verbose_name_plural = _("réalisateurs")
