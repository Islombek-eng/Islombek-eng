from django.urls import path
from . import views

urlpatterns = [
    path('',  views.home_page),
    path('/products/<int;pk>', views.product_page),
    path('/category/<int:pk>', views.product_page)
]