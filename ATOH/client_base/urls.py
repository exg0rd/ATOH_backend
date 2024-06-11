from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_users, name='get_users'),
     path('sorted/', views.get_sorted_users, name='get_sorted_users'),
]