from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReservaForm
from .models import Sala, Reserva
from datetime import datetime, timedelta
from dateutil.relativedelta import *

# Create your views here.
# Templates que serão visualizados no site

# garante que uma pessoa só pode entrar nessa página se estiver logada
# se não estiver, é redirecionada para a tela de login
@staff_member_required
def index(request):
    # o request method é como entramos nessa página:
    # GET: seria entrar digitando a url no browser ou clicando em um link
    # POST: o method que colocamos no formulário (olhar a tag form no index.html)
    #       então será POST se submetermos o formulário
    if request.method == 'POST':
        # Criação da variável 'form' para receber os dados do formulário djreservas via post:
        form = ReservaForm(request.POST)
        
        # Validação do Formulário do site com o Banco de Dados criado:
        if form.is_valid():
            reserva = Reserva()
            
            # A data vem em formato texto do formulário
            data_reserva_texto = form.data["data_reserva"]
            # aqui é convertida para ser uma data do django
            data_reserva = datetime.strptime(data_reserva_texto, "%d/%m/%Y")
            # só então colocamos ela na reserva que será salva no banco
            reserva.data_reserva = data_reserva

            # o formato de hora vem certo do formulário, por isso não precisa de conversão
            reserva.hora_inicio = form.data["hora_inicio"]
            reserva.hora_fim = form.data["hora_fim"]

            reserva.motivo = form.data["motivo"]
            
            # O que vem no formulário é o ID da sala
            sala_id = form.data["sala"]
            # como precisamos da sala em si para colocar na reserva, buscamos no banco pelo id
            salas = Sala.objects.filter(id = sala_id)
            # o filtro devolve uma lista com um item só, pegamos o primeiro item
            reserva.sala = salas[0]

            # esse usuário que está no request é o usuário que está logado
            reserva.responsavel_cliente = request.user

            reserva.save()

    # Criação da condição para o formulário ficar em branco
    else:
        form = ReservaForm()

    # Listagem de sala para o Select (pega todas as salas do banco de dados):
    salas = Sala.objects.all()
    
    hoje = datetime.today()
    
    # pega o que será exibido no topo do calendário (ex: "Outubro - 2019")
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro",
     "Outubro", "Novembro","Dezembro"]
    nome_mes = meses[hoje.month-1] + " - " + str(hoje.year)
    
    semana = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
    
    # para calcular quando começa e quando termina o calendário
    primeiro_dia = hoje - timedelta(days = hoje.day-1)
    primeiro_dia_seguinte = primeiro_dia + relativedelta(months = 1)
    ultimo_dia = primeiro_dia_seguinte - timedelta(days = 1)

    dias_antes = primeiro_dia.weekday() + 1 % 7
    dias_depois = 6 - (ultimo_dia.weekday() + 1 % 7)
    
    vetor_dias = []
    for d in range(dias_antes, 0, -1):
        dia = primeiro_dia - relativedelta(days = d)
        vetor_dias.append(dia)
    for d in range(primeiro_dia.day, ultimo_dia.day + 1):
        dia = primeiro_dia + relativedelta(days = d - 1)
        vetor_dias.append(dia)
    for d in range(1, dias_depois + 1):
        dia = ultimo_dia + relativedelta(days = d)
        vetor_dias.append(dia)

    mes = hoje.month

    # Retorno na tela
    return render(request, 'djreservas/index.html', {'form': form, 'salas': salas, 'email': request.user.email,
     'nome_mes': nome_mes, 'semana': semana, 'dias': vetor_dias, 'mes': mes})

@staff_member_required
def forms(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        # Criação da condição para a validação do formulário
        form = ReservaForm(request.POST)
        # check whether it's valid:
        # Checagem da validação dos itens no formulário
        if form.is_valid():
            reserva = Reserva()
            
            data_reserva_texto = form.data["data_reserva"]
            data_reserva = datetime.strptime(data_reserva_texto, "%d/%m/%Y")
            reserva.hora_inicio = form.data["hora_inicio"]
            reserva.hora_fim = form.data["hora_fim"]
            reserva.motivo = form.data["motivo"]

            salas = Sala.objects.filter(id = form.data["sala"])
            reserva.sala = salas[0]
            reserva.responsavel_cliente = request.user
            reserva.data_reserva = data_reserva
            reserva.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #return HttpResponseRedirect('/thanks/')


    # if a GET (or any other method) we'll create a blank form
    # Criação da condição para o formulário ficar em branco.
    else:
        form = ReservaForm()

    salas = Sala.objects.all()
    return render(request, 'djreservas/forms.html', {'form': form, 'salas': salas, 'email': request.user.email})