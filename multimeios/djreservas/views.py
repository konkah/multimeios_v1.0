from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReservaForm, DataForm
from .models import Sala, Reserva

# Create your views here.
# Templates que serão visualizados no site

def index(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        # Criação da condição para a validação do formulário
        form = ReservaForm(request.POST)
        # check whether it's valid:
        # Checagem da validação dos itens no formulário
        if form.is_valid():
            reserva = Reserva()
            
            reserva.data_reserva = form.data["data_reserva"]
            reserva.hora_inicio = form.data["hora_inicio"]
            reserva.hora_fim = form.data["hora_fim"]
            reserva.motivo = form.data["motivo"]
            
            salas = Sala.objects.filter(id = form.data["sala"])
            reserva.sala = salas[0]
            reserva.responsavel_cliente = request.user
            #reserva.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    # Criação da condição para o formulário ficar em branco.
    else:
        form = ReservaForm()

    salas = Sala.objects.all()
    return render(request, 'djreservas/index.html', {'form': form, 'salas': salas})

def forms(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        # Criação da condição para a validação do formulário
        form = ReservaForm(request.POST)
        # check whether it's valid:
        # Checagem da validação dos itens no formulário
        if form.is_valid():
            reserva = Reserva()
            
            reserva.data_reserva = form.data["data_reserva"]
            reserva.hora_inicio = form.data["hora_inicio"]
            reserva.hora_fim = form.data["hora_fim"]
            reserva.motivo = form.data["motivo"]
            #reserva.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    # Criação da condição para o formulário ficar em branco.
    else:
        form = ReservaForm()

    salas = Sala.objects.all()
    return render(request, 'djreservas/forms.html', {'form': form, 'salas': salas})