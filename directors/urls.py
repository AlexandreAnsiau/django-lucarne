from django.urls import path
from django.utils.translation import gettext_lazy as _

from .views import DirectorView

urlpatterns = [
    path(_("<int:pk>/"), DirectorView.as_view(), name="director"),
]
