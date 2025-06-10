from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('add/', views.add_project, name='add_project'), 
    path('edit/<int:pk>/', views.edit_project, name='edit_project'),
   
]