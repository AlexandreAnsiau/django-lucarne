from django.urls import path
from django.utils.translation import gettext_lazy as _

from .views import CategoryView, CategoriesView, VideoView

urlpatterns = [
    path(_("categories/<int:pk>/"), CategoryView.as_view(), name="category"),
    path(_("<int:pk>/"), VideoView.as_view(), name="video")
]