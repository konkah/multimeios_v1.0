from django.urls import path

from . import views

# Nome do arquivo na url do Browser

app_name = 'djreservas'
urlpatterns = [
    path('', views.index, name='index'),
    path('forms/', views.forms, name='forms'),
    path('calendario/<int:ano_mes>/<int:sala_id>/', views.calendario, name='calendario'),
    path('calendario/<int:ano_mes>/', views.calendario_todas, name='calendario_todas'),
    path('calendario/', views.calendario_hoje, name='calendario_hoje'),
    path('success/', views.success, name='success'),
    path('aprovar/<int:reserva_id>/',views.aprovar, name='aprovar'),
    path('reprovar/<int:reserva_id>/',views.reprovar, name='reprovar'),
]