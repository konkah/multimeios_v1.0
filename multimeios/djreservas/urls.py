from django.urls import path

from . import views

app_name = 'djreservas'
urlpatterns = [
    path('', views.index, name='index'),
]