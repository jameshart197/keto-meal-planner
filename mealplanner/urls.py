from . import views
from django.urls import path

urlpatterns = [
    path('', views.meal_list(request).as_view(), name='meal_list'),
]