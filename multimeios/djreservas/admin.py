from django.contrib import admin

# Register your models here.
from .models import Grupo, Cliente, Sala, Reserva

# Modelos colocados no Django-Admin

admin.site.register(Grupo)
admin.site.register(Cliente)
admin.site.register(Sala)
admin.site.register(Reserva)