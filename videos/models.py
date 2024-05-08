from admin_ordering.models import OrderableModel
from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import FileModel


class Category(FileModel):
    name = models.CharField(max_length=200, unique=True)
    # Videos of presentation are uploaded in presentation_videos/ placed in the directory asigns to the setting constant MEDIA_ROOT
    presentation_video = models.FileField(upload_to="presentation_videos/", null=True, blank=True, verbose_name=_("video de présentation"))  # must add help text
    is_visible = models.Boolean(default=False)

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
