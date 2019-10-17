from django.contrib import admin

# Register your models here.
from .models import Sala, Reserva

# Modelos colocados no Django-Admin

admin.site.register(Sala)
admin.site.register(Reserva)