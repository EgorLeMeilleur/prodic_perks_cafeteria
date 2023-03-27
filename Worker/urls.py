from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('auth/', views.home, name='home'),
    path('personal_cabinet/', views.personal_cabinet, name='personal_cabinet'),
    path('logout/', views.logout, name='logout')
]
