from django.contrib import admin 
from django.urls import path 
from . import views 
  
urlpatterns = [ 
    path('', views.restaurant, name='index'),
    path('menu/', views.MenuView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view())
]