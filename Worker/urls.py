from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('auth/', views.home, name='home'),
    path('personal_cabinet/profile', views.personal_cabinet, name='personal_cabinet'),
    path('logout/', views.logout, name='logout'),
    path('bought/<int:pk>/', views.bought, name='bought'),
    path('wished/<int:pk>/', views.wished, name='wished'),
    path('wished_remove/<int:pk>/', views.wished_remove, name='wished_remove'),
    path('delete_benefit/<int:pk>/', views.delete_benefit, name='delete_benefit'),
    path('delete_worker/<int:pk>/', views.delete_worker, name='delete_worker'),
    path('personal_cabinet/list_of_wishes', views.wished_show, name='wished_show'),
    path('personal_cabinet/list_of_benefits', views.sort_by_popularity, name='benefits_show'),
    path('personal_cabinet/list_of_employees', views.employees_show, name='employees_show'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('add_benefit/', views.add_benefit, name='add_benefit'),
    path('sort_by_price/', views.sort_by_price_asc, name="sort_by_price"),
    path('sort_by_city/', views.sort_by_сity, name='sort_by_city'),
    path('sort_by_popularity/', views.sort_by_popularity, name='sort_by_popularity'),
    path('faq/', views.faq, name='faq'),
    path('', views.beginning_page, name='beginning_page')
]
