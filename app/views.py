from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Task


def index(request):
    return render(request, 'app/index.html')


class HomeView(ListView):
    context_object_name = 'tasks'
    template_name = 'app/index.html'
    model = Task
