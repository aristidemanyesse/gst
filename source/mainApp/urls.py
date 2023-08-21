from django.urls import path

from . import views

app_name = "mainApp"
urlpatterns = [
    path('', views.main, name='main'),
    path('services/', views.services, name='services'),
    path('contacts/', views.contacts, name='contacts'),
]