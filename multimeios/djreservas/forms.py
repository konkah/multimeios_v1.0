from django import forms

class ReservaForm(forms.Form):
    data_reserva = forms.DateField()
    hora_inicio = forms.TimeField()
    hora_fim = forms.TimeField()
    sala = forms.IntegerField()
    motivo = forms.CharField()
    