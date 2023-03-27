from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('auth/', views.home, name='home'),
    path('logged/', views.logged, name='logged'),
    path('logout/', views.logout, name='logout')
]
