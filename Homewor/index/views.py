from django.shortcuts import render

# Create your views here.

from django.urls import path
from . import views

urlpatterns = (
    # ... другие ваши URL-ы
)

from django.shortcuts import render
from .models import News

def news_list(request):
    news_list = News.objects.all()
    return render(request, 'news_list.html', {'news_list': news_list})