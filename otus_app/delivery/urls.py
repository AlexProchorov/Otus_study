from django.urls import path
from .views import create_storage

urlpatterns = [
    path('create_storage/<int:pk>/', create_storage, name='storage'),


]