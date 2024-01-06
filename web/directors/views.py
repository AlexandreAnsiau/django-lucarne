from unicodedata import category
from django.shortcuts import redirect, render
from django.views.generic import DetailView, FormView, ListView, View

from .forms import EmailForm
from .models import Category, Contact, CustomUser, Video


class EmailSenderView(FormView):
    template_name = "index.html"
    form_class = EmailForm

    def form_valid(self, form):
        form.send_email()
        return redirect("index")


class IndexView(ListView):
    model = Category
    context_object_name = "categories"
    template_name = "index.html"

    def get_queryset(self):
        categories_order = ["cinema", "clips", "arts", "branding"]
        return [Category.objects.get(name__iexact=category_name) for category_name in categories_order]


class CategoryView(DetailView):
    model = Category
    context_object_name = "category"
    template_name = "category_detail.html"


class DirectorView(DetailView):
    model = CustomUser
    context_object_name = "director"
    template_name = "director_detail.html"


class ContactView(ListView):
    model = Contact
    context_object_name = "contacts"
    template_name = "contact.html"


class VideoView(DetailView):
    model = Video
    context_object_name = "video"
    template_name = "video_detail.html"
