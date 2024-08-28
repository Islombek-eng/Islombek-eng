from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class Cart(models.Model):
    product = models.CharField(max_length=255)  # Можно использовать ForeignKey для связи с моделью товара
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_count = models.PositiveIntegerField()
    created_at = models.DateTimeField(default=timezone.now)

class NewsCategory(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

class News(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

