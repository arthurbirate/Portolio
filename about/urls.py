from django.urls import path
from .views import about_me_view
from .views import add_about

urlpatterns = [
    path('', about_me_view, name='about_me'),
    path('add/', add_about, name='add_about')
    
]
