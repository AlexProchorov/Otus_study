from django.urls import path
from .views import depositmoney,withdrawmoney,payfororder

urlpatterns = [
    path('depositmoney/<int:pk>/', depositmoney, name='deposit'),
    path('withdrawmoney/<int:pk>/', withdrawmoney, name='withdrawmoney'),
    path('payfororder/<int:pk>/', payfororder, name='payfororder'),
]