from django import forms

# Criação dos Formulários com base nos modelos do banco de dados

class DataForm(forms.Form):
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )

class ReservaForm(forms.Form):
    data_reserva = forms.DateField(input_formats=['%d/%m/%Y'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        }))
    hora_inicio = forms.TimeField()
    hora_fim = forms.TimeField()
    sala = forms.IntegerField()
    motivo = forms.CharField()
    