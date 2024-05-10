from django.urls import path

from videos.views import CategoriesView

urlpatterns = [
    path("", CategoriesView.as_view(), name="index")
]