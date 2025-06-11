from django.urls import path
from .views import internship_view
from .views import add_internship, edit_internship

urlpatterns = [
    path('', internship_view, name='internship'),
      path('add/', add_internship, name='add_internship'),
       path('edit/<int:pk>/', edit_internship, name='edit_internship'),
]
