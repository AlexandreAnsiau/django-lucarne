from asyncio.log import logger
from admin_ordering.models import OrderableModel
from django.db import migrations, models, transaction
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager
from common.models import FileModel


class DisplayerNone:

    def __getattribute__(self, attr):
        if super().__getattribute__(attr) is None:
            return ""
        return super().__getattribute__(attr)


class CustomUser(OrderableModel, FileModel, AbstractUser):
    username = None
    email = models.EmailField(max_length=500, unique=True)
    is_active = models.BooleanField(blank=True, default=True)
    is_staff = models.BooleanField(blank=True, default=True)
    is_superuser = models.BooleanField(blank=True, default=True)
    first_name = models.CharField(max_length=100, verbose_name=_("prénom"))
    last_name = models.CharField(max_length=100, verbose_name=_("nom de famille"))
    description = models.TextField(max_length=1000, verbose_name=_("description"), blank=True)
    profil_image = models.ImageField(upload_to="profil_images/", null=True, blank=True, verbose_name=_("photo de profil"))
    phone_number = models.CharField(max_length=30, blank=True, verbose_name=_("num de tel"))
    job = models.CharField(max_length=100, verbose_name=_("métier"), blank=True)
    slug = models.SlugField()

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


class Category(FileModel):
    name = models.CharField(max_length=200, unique=True)
    # Videos of presentation are uploaded in presentation_videos/ placed in the directory asigns to the setting constant MEDIA_ROOT
    presentation_video = models.FileField(upload_to="presentation_videos/", null=True, blank=True, verbose_name=_("video de présentation"))  # must add help text

    class Meta:
        verbose_name = _("catégorie")
        verbose_name_plural = _("catégories")

    def __str__(self):
        return self.name


class Video(OrderableModel, FileModel):
    name = models.CharField(max_length=500, verbose_name=_("nom"))
    video = models.FileField(upload_to="videos/")  # Videos are uploaded in videos/ placed in the directory asigns to the setting constant MEDIA_ROOT
    directors = models.ManyToManyField("CustomUser", related_name="videos", verbose_name=_("réalisateurs"))
    categories = models.ManyToManyField("Category", related_name="videos")
    description = models.TextField(max_length=1000, blank=True)
    presentation_video = models.FileField(upload_to="presentation_resume_video/", null=True, blank=True, verbose_name=_("video de présentation"))  # must add help text

    class Meta(OrderableModel.Meta):
        verbose_name = _("vidéo")
        verbose_name_plural = _("vidéos")

    def __str__(self):
        return self.name


class Screenshot(OrderableModel, models.Model):
    video = models.ForeignKey("Video", on_delete=models.CASCADE, related_name="screenshots")
    screenshot = models.ImageField(upload_to="screenshot")  # Screenshots are uploaded in screenshot/ placed in the directory asigns to the setting constant MEDIA_ROOT


# class Foto(models.Model):
#     name = models.CharField(max_length=500, verbose_name=_("nom"))
#     foto = models.FileField(upload_to="fotos/", verbose_name=_("photo"))
#     directors = models.ManyToManyField("CustomUser", related_name="fotos", verbose_name=_("réalisateur"))
#     categories = models.ManyToManyField("Category", blank=True)
#
#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)
#         foto_category = Category.objects.filter(name="photo")
#         self.categories.set(foto_category)
#         super().save(*args, **kwargs)
#
#     class Meta:
#         verbose_name = _("Photo")
#         verbose_name_plural = _("Photos")
#
#     def __str__(self):
#         return self.name


class Contact(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("nom"))
    url = models.URLField(max_length=500, null=True, blank=True)
    logo = models.ImageField(upload_to="contact_logo/", null=True, blank=True)

    def __str__(self):
        return self.name


# populating of Category
try:
    categories = ["cinema", "clips", "arts", "branding"]
    for category in categories:
        Category.objects.get_or_create(name=category)
except:  # noqa: E722
    pass
