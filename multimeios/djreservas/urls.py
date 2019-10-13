from django.urls import path

from . import views

# Nome do arquivo na url do Browser

app_name = 'djreservas'
urlpatterns = [
    path('', views.index, name='index'),
]