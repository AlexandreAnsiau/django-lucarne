from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from .views import (CategoryView, ContactView, DirectorView, EmailSenderView,
                    IndexView, VideoView)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path(_("categorie/<int:pk>"), CategoryView.as_view(), name="category"),
    path(_("realisateur/<int:pk>"), DirectorView.as_view(), name="director"),
    path(_("video/<int:pk>"), VideoView.as_view(), name="video")
    # path(_("email-sender"), EmailSenderView.as_view(), name="email_sender"),  # should only accept post request
    # path(_("contact"), ContactView.as_view(), name="contact"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
