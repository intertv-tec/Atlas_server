from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    
    path('register/', views.register_automation, name='register_automation'),
    path('ping/<int:pk>/<str:key>/', views.ping_automation, name='ping_automation'),
    path('',views.home,name='home')
]
