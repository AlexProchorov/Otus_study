from django.urls import path
from .views import create_order

urlpatterns = [
    path('create/<int:pk>/', create_order, name='order'),


]