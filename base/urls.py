from django.urls import path
from . import views

urlpatterns = [path('', views.home ,name = 'home'),
path('add/', views.addTodo, name='add_todo'),
path('delete/<int:pk>/', views.delete, name='delete'),
]