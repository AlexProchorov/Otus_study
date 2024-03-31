from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('create/', views.add_user, name='add-items'),
    path('all/', views.view_users, name='view_items'),
    path('update/<int:pk>/', views.update_user, name='update-items'),
    path('users/<int:pk>/delete/', views.delete_items, name='delete-items'),
]