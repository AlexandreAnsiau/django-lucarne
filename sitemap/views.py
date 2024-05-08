from django.contrib import sitemaps
from django.urls import reverse

from directors.models import Director
from videos.models import Category, Video

# Create your views here.

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "weekly"
    i18n = True

    def items(self):
        return ["index"]

    def location(self, item):
        return reverse(item)


class CategoriesViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "weekly"
    i18n = True

    def items(self):
        return Category.objects.all()

    def location(self, item):
        return reverse("category", kwargs={"pk": item.id})


class VideosViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "weekly"
    i18n = True

    def items(self):
        return Video.objects.all()

    def location(self, item):
        return reverse("video", kwargs={"pk": item.id})


class DirectorsViewSitemap(sitemaps.Sitemap):
        priority = 0.5
        changefreq = "weekly"
        i18n = True

        def items(self):
            return Director.objects.all()

        def location(self, item):
            return reverse("director", kwargs={"pk": item.id})