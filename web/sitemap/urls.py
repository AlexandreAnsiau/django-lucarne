from django.contrib.sitemaps import views
from django.urls import path

from .views import (CategoriesViewSitemap, DirectorsViewSitemap, StaticViewSitemap,
                    VideosViewSitemap)

sitemaps = {
    "category": CategoriesViewSitemap,
    "directors": DirectorsViewSitemap,
    "video": VideosViewSitemap,
    "static": StaticViewSitemap
}

urlpatterns = [
    path("sitemap.xml", views.index, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.index"),
    path("sitemap-<section>.xml", views.sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap")
]
