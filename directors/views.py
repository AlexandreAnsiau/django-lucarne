from django.shortcuts import render
from django.views.generic import DetailView

from .models import Director


class DirectorView(DetailView):
    model = Director
    context_object_name = "director"
    template_name = "directors/director.html"