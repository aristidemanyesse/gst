from django.urls import path

from . import views

app_name = "mainApp"
urlpatterns = [
    path('', views.main, name='main'),
    path('services/', views.services, name='services'),
    path('contacts/', views.contacts, name='contacts'),
    
    path('admin/', views.login_, name='login'),
    path('admin/login/', views.login_, name='login'),
    path('admin/connexion/', views.connexion, name='connexion'),
    
    path('admin/liste/', views.liste, name='liste'),
]