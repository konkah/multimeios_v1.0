from django import forms

# Criação dos Formulários com base nos modelos do banco de dados

class ReservaForm(forms.Form):
    data_reserva = forms.DateField(input_formats=['%d/%m/%Y'])
    hora_inicio = forms.TimeField()
    hora_fim = forms.TimeField()
    sala = forms.IntegerField()
    motivo = forms.CharField()
    