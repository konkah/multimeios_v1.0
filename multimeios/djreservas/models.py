from django.db import models

# Create your models here.
class Grupo(models.Model):
    nome = models.CharField(max_length=200)
    patrocinio = models.CharField(max_length=200)

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    permissao = models.CharField(max_length=20)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)

class Sala(models.Model):
    nome = models.CharField(max_length=200)
    local = models.IntegerField(default=0)
    capacidade = models.IntegerField(default=0)
    recursos_fixos = models.CharField(max_length=2000)

class Reserva(models.Model):
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    responsavel_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_reserva = models.DateTimeField('Data da Reserva')
    data_inicio = models.DateTimeField('Hora Início')
    data_final = models.DateTimeField('Hora Fim')
    recursos_necessarios = models.CharField(max_length=2000)
    aprovacao = models.BooleanField()
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)

