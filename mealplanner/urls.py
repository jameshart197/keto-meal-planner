from . import views
from django.urls import path

urlpatterns = [
    path('', views.meal_list, name='meal_list'),
    path('home/', views.home, name='home'),
    path('adminpanel/', views.adminpanel, name='adminpanel'),
]