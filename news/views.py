from django.shortcuts import render
from .models import News

def news(request):
    newss = News.objects.all()
    return render(request, 'news/news_page.html', {'newss': newss})
