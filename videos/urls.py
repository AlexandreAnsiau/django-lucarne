from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from .views import CategoryView, CategoriesView, VideoView

urlpatterns = [
    path("", CategoriesView.as_view(), name="index"),
    path(_("categorie/<int:pk>"), CategoryView.as_view(), name="category"),
    path(_("video/<int:pk>"), VideoView.as_view(), name="video")
]