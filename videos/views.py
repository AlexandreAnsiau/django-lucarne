from django.views.generic import DetailView, ListView

from .models import Category, Video


class CategoriesView(ListView):
    model = Category
    context_object_name = "categories"
    template_name = "videos/categories.html"

    def get_queryset(self):
        return self.model.objects.filter(is_visible=True)


class CategoryView(DetailView):
    model = Category
    context_object_name = "category"
    template_name = "videos/category_detail.html"


class VideoView(DetailView):
    model = Video
    context_object_name = "video"
    template_name = "videos/video_detail.html"