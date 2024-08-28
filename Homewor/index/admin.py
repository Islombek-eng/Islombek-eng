from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Cart, NewsCategory, News

admin.site.register(Cart)
admin.site.register(NewsCategory)
admin.site.register(News)