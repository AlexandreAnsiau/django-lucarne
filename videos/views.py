from django.views.generic import DetailView, ListView

from .models import Category, Video


class CategoriesView(ListView):
    model = Category
    context_object_name = "categories"
    template_name = "index.html"

    def get_queryset(self):
        return self.model.filter(is_visible=True)


class CategoryView(DetailView):
    model = Category
    context_object_name = "category"
    template_name = "category_detail.html"


class VideoView(DetailView):
    model = Video
    context_object_name = "video"
    template_name = "video_detail.html"