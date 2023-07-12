from . import views
from django.urls import path

urlpatterns = [
    path('', views.meal_list, name='meal_list'),
    path('home/', views.home, name='home'),
    path('adminpanel/', views.adminpanel, name='adminpanel'),
    path('adminpanel/add', views.add_adminpanel, name='add_adminpanel'),
    path('adminpanel/edit', views.edit_adminpanel, name='edit_adminpanel'),
    path('adminpanel/delete', views.delete_adminpanel, name='delete_adminpanel'),
]