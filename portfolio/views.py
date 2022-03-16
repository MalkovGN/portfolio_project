from django.shortcuts import render
from .models import Project


def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})


def all_blogs(request):
    return render(request, 'blog/all_blogs.html')


def news(requests):
    return render(requests, 'news/news_page.html')

