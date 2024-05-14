from admin_ordering.models import OrderableModel
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager
from common.models import FileModel


class CustomUser(OrderableModel, FileModel, AbstractUser):
    username = None
    email = models.EmailField(max_length=500, unique=True)
    is_active = models.BooleanField(blank=True, default=True)
    is_staff = models.BooleanField(blank=True, default=False)
    is_superuser = models.BooleanField(blank=True, default=False)
    first_name = models.CharField(max_length=100, verbose_name=_("prénom"))
    last_name = models.CharField(max_length=100, verbose_name=_("nom de famille"))
    slug = models.SlugField()
    description = models.TextField(max_length=1000, verbose_name=_("description"), blank=True)
    profile_image = models.ImageField(upload_to="profile_images/", null=True, blank=True,
                                      default="default/profile_images/user.png", verbose_name=_("photo de profil"))
    phone_number = models.CharField(max_length=30, blank=True, verbose_name=_("num de tel"))
    job = models.CharField(max_length=100, verbose_name=_("métier"), blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta(OrderableModel.Meta):
        verbose_name = _("utilisateur")
        verbose_name_plural = _("utilisateurs")

    def save(self, **kwargs):
        self.slug = slugify(f"{self.first_name}-{self.last_name}")
        super().save(**kwargs)

    def __str__(self):
        return f"{self.first_name.title()} {self.last_name.title()}"