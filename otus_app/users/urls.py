from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('add', views.add, name='add'),
    path('delete/<int:ID>/', views.delete, name='delete'),
    path('update/<int:ID>/', views.update, name='update'),
    path('update/uprec/<int:ID>/', views.uprec, name='uprec')
]