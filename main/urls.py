from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('registration', views.registration),
    path('auth', views.auth),
    path('adminGuide', views.adminGuide),
    path('employmentGuide', views.employmentGuide),
]