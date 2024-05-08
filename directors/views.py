from django.shortcuts import render
from django.views.generic import DetailView

from .models import CustomUser


class DirectorView(DetailView):
    model = CustomUser
    context_object_name = "director"
    template_name = "director_detail.html"