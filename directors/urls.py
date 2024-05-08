from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from .views import (CategoryView, ContactView, DirectorView, EmailSenderView,
                    IndexView, VideoView)

urlpatterns = [
    path(_("realisateur/<int:pk>"), DirectorView.as_view(), name="director"),
]
