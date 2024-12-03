from django.urls import path
from app_base import views

urlpatterns = [
    #inicio jugueteria
    path('', views.inicio, name='inicio'),
]
