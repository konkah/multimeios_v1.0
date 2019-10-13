from django.db import models
import datetime

# Create your models here.
class Grupo(models.Model):
    nome = models.CharField(max_length=200)
    patrocinio = models.CharField(max_length=200)

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    permissao = models.CharField(max_length=20)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)

class Sala(models.Model):
    nome = models.CharField('Nome da Sala',max_length=200)
    capacidade = models.IntegerField('Capacidade de Pessoas', default=0)
    recursos_fixos = models.CharField('Recursos Fixos', max_length=2000)

class Reserva(models.Model):
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    responsavel_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_reserva = models.DateField('Data da Reserva') #date or #datetime
    hora_inicio = models.TimeField('Hora Início', default=datetime.time(0, 00)) #time | -----
    hora_fim = models.TimeField('Hora Fim', default=datetime.time(0, 00)) #time | time
    motivo = models.CharField(max_length=2000)
    aprovacao = models.BooleanField('Aprovação')
    

