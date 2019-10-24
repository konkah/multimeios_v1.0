from django.urls import path

from . import views

# Nome do arquivo na url do Browser

app_name = 'djreservas'
urlpatterns = [
    path('', views.index, name='index'),
    path('forms/', views.forms, name='forms'),
    path('calendario/', views.calendario, name='calendario'),
    path('password/', views.password, name='password'),
    path('success/', views.success, name='success'),
]