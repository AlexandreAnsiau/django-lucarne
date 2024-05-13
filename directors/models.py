from django.db import models
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

from .managers import DirectorManager
from registrations.models import CustomUser


class Director(CustomUser):

    objects = DirectorManager()

    def save(self, *args, **kwargs):
        self.is_staff = True
        super().save(*args, **kwargs)
        directors = Group.objects.filter(name="directors").first()
        directors.user_set.add(self)


    class Meta:
        proxy = True
        verbose_name = _("réalisateur")
        verbose_name_plural = _("réalisateurs")
