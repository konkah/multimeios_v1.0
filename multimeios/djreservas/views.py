from django.utils.translation import ugettext as _
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.forms.utils import ErrorList
from .forms import ReservaForm
from .models import Sala, Reserva
from datetime import datetime
from dateutil.relativedelta import *

# Create your views here.
# Templates que serão visualizados no site

# garante que uma pessoa só pode entrar nessa página se estiver logada
# se não estiver, é redirecionada para a tela de login

@staff_member_required(login_url='/conta/login')
def success(request):
    return render(request, 'djreservas/success.html')

@staff_member_required(login_url='/conta/login')
def index(request):
    hoje = datetime.now().date()
    agora = datetime.now().time()
    mes_seguinte = hoje + relativedelta(months=1)

    return render(request, 'djreservas/index.html')

@staff_member_required(login_url='/conta/login')
def forms(request):
    reservas_feitas = []
    hoje = datetime.now().date()
    agora = datetime.now().time()
    mes_seguinte = hoje + relativedelta(months=1)
    # o request method é como entramos nessa página:
    # GET: seria entrar digitando a url no browser ou clicando em um link
    # POST: o method que colocamos no formulário (olhar a tag form no index.html)
    #       então será POST se submetermos o formulário
    if request.method == 'POST':
        # Criação da variável 'form' para receber os dados do formulário djreservas via post:
        form = ReservaForm(request.POST)
        
        # O que vem no formulário é o ID da sala
        sala_id = form.data["sala"]
        if sala_id == "0" or sala_id == '' or sala_id == None:
            form.add_error("sala", "Por favor, escolha uma sala.")

        # A data vem em formato texto do formulário
        data_reserva_texto = form.data["data_reserva"]
        if data_reserva_texto != '':
            # Aqui é convertida para ser uma data do django
            data_reserva = datetime.strptime(data_reserva_texto, "%d/%m/%Y")
        # A hora de início vem em formato texto do formulário
        hora_inicio_texto = form.data["hora_inicio"]
        if hora_inicio_texto != '':
            # Aqui é convertida para ser uma hora do django
            hora_inicio = datetime.strptime(hora_inicio_texto, "%H:%M").time()
        # A hora de fim vem em formato texto do formulário
        hora_fim_texto = form.data["hora_fim"]
        if hora_fim_texto != '':
            # Aqui é convertida para ser uma hora do django
            hora_fim = datetime.strptime(hora_fim_texto, "%H:%M").time()

        #Validações das Reservas
        if data_reserva_texto != '':
            reservas_feitas = Reserva.objects.filter(data_reserva=data_reserva, aprovacao=True, sala__id=sala_id)
            if data_reserva.date() < hoje:
                form.add_error("data_reserva", "Não é possível reservar datas passadas.")
            elif data_reserva.weekday() == 6 or data_reserva.weekday() == 5:
                form.add_error("data_reserva", "Não é possível reservar nos sábados ou domingos.")
            elif data_reserva.date() > mes_seguinte:
                form.add_error("data_reserva", "Reserva não pode ser feita com mais de 1 mês de antecedência.")
            elif hora_inicio_texto != '' and hora_fim_texto != '':
                for reserva_feita in reservas_feitas:
                    if reserva_feita.hora_fim > hora_inicio and reserva_feita.hora_inicio < hora_fim:
                        form.add_error("", "Já existe reserva para esta sala, nesta data e horário.")
                        break
                if data_reserva.date() == hoje and hora_inicio < agora:
                    form.add_error("hora_inicio", "Não é possível reservar horas passadas.")
                elif hora_inicio >= hora_fim:
                    form.add_error("hora_inicio", "A hora final precisa ser posterior à hora de início.")

        # Validação do Formulário do site com o Banco de Dados criado:
        if form.is_valid():
            reserva = Reserva()
            
            # só então colocamos ela na reserva que será salva no banco
            reserva.data_reserva = data_reserva

            # o formato de hora vem certo do formulário, por isso não precisa de conversão
            reserva.hora_inicio = form.data["hora_inicio"]
            reserva.hora_fim = form.data["hora_fim"]

            reserva.motivo = form.data["motivo"]
            
            # como precisamos da sala em si para colocar na reserva, buscamos no banco pelo id
            salas = Sala.objects.filter(id = sala_id)
            # o filtro devolve uma lista com um item só, pegamos o primeiro item
            reserva.sala = salas[0]

            # esse usuário que está no request é o usuário que está logado
            reserva.responsavel_cliente = request.user

            reserva.save()
            return HttpResponseRedirect(reverse('djreservas:success'))

    # Criação da condição para o formulário ficar em branco
    else:
        form = ReservaForm()

    # Listagem de sala para o Select (pega todas as salas do banco de dados):
    salas = Sala.objects.all()
    
    # pega o que será exibido no topo do calendário (ex: "Outubro - 2019")
    
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro",
     "Outubro", "Novembro","Dezembro"]
    nome_mes = meses[hoje.month-1] + " - " + str(hoje.year)
    semana = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
    
    # Para calcular quando começa e quando termina o calendário
    primeiro_dia = hoje - relativedelta(days = hoje.day-1)
    primeiro_dia_seguinte = primeiro_dia + relativedelta(months = 1)
    ultimo_dia = primeiro_dia_seguinte - relativedelta(days = 1)

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
    
    # Listagem de sala para o Select (pega todas as salas do banco de dados):
    primeira_data_reserva = datetime.combine(vetor_dias[0], datetime.min.time())
    ultima_data_reserva = datetime.combine(vetor_dias[-1], datetime.min.time())
    reservas = Reserva.objects.filter(
        data_reserva__range = [primeira_data_reserva, ultima_data_reserva]
    )
    
    calendario = []
    for dia in vetor_dias:
        reservas_dia=reservas.filter(data_reserva=dia)
        data  = {'dia':dia, 'reservas':reservas_dia}
        calendario.append(data)
    
    # Retorno na tela
    return render(request, 'djreservas/forms.html', {
        'form': form, 
        'salas': salas, 
        'email': request.user.email,
        'nome_mes': nome_mes, 
        'semana': semana, 
        'mes': mes, 
        'hoje': hoje,
        'calendario': calendario,
        'reservas_feitas': reservas_feitas,
    })

@staff_member_required(login_url='/conta/login')
def calendario(request):
    hoje = datetime.now().date()
    agora = datetime.now().time()
    mes_seguinte = hoje + relativedelta(months=1)
    # o request method é como entramos nessa página:
    # GET: seria entrar digitando a url no browser ou clicando em um link
    # POST: o method que colocamos no formulário (olhar a tag form no index.html)
    #       então será POST se submetermos o formulário
    if request.method == 'POST':
        # Criação da variável 'form' para receber os dados do formulário djreservas via post:
        form = ReservaForm(request.POST)
        
        # O que vem no formulário é o ID da sala
        sala_id = form.data["sala"]
        if sala_id == "0" or sala_id == '' or sala_id == None:
            form.add_error("sala", "Por favor, escolha uma sala.")

        # A data vem em formato texto do formulário
        data_reserva_texto = form.data["data_reserva"]
        if data_reserva_texto != '':
            # Aqui é convertida para ser uma data do django
            data_reserva = datetime.strptime(data_reserva_texto, "%d/%m/%Y")
        # A hora de início vem em formato texto do formulário
        hora_inicio_texto = form.data["hora_inicio"]
        if hora_inicio_texto != '':
            # Aqui é convertida para ser uma hora do django
            hora_inicio = datetime.strptime(hora_inicio_texto, "%H:%M")
        # A hora de fim vem em formato texto do formulário
        hora_fim_texto = form.data["hora_fim"]
        if hora_fim_texto != '':
            # Aqui é convertida para ser uma hora do django
            hora_fim = datetime.strptime(hora_fim_texto, "%H:%M")
        
        #Validações das Reservas
        if data_reserva_texto != '':
            if data_reserva.date() < hoje:
                form.add_error("data_reserva", "Não é possível reservar datas passadas.")
            elif data_reserva.weekday() == 6 or data_reserva.weekday() == 5:
                form.add_error("data_reserva", "Não é possível reservar nos sábados ou domingos.")
            elif data_reserva.date() > mes_seguinte:
                form.add_error("data_reserva", "Reserva não pode ser feita com mais de 1 mês de antecedência.")
            elif hora_inicio_texto != '' and hora_fim_texto != '':
                if data_reserva.date() == hoje and hora_inicio.time() < agora:
                    form.add_error("hora_inicio", "Não é possível reservar horas passadas.")
                elif hora_inicio >= hora_fim:
                    form.add_error("hora_inicio", "A hora final precisa ser posterior à hora de início.")

        # Validação do Formulário do site com o Banco de Dados criado:
        if form.is_valid():
            reserva = Reserva()
            
            # só então colocamos ela na reserva que será salva no banco
            reserva.data_reserva = data_reserva

            # o formato de hora vem certo do formulário, por isso não precisa de conversão
            reserva.hora_inicio = form.data["hora_inicio"]
            reserva.hora_fim = form.data["hora_fim"]

            reserva.motivo = form.data["motivo"]
            
            # como precisamos da sala em si para colocar na reserva, buscamos no banco pelo id
            salas = Sala.objects.filter(id = sala_id)
            # o filtro devolve uma lista com um item só, pegamos o primeiro item
            reserva.sala = salas[0]

            # esse usuário que está no request é o usuário que está logado
            reserva.responsavel_cliente = request.user

            reserva.save()
            return HttpResponseRedirect(reverse('djreservas:index'))

    # Criação da condição para o formulário ficar em branco
    else:
        form = ReservaForm()

    # Listagem de sala para o Select (pega todas as salas do banco de dados):
    salas = Sala.objects.all()
    
    # pega o que será exibido no topo do calendário (ex: "Outubro - 2019")
    
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro",
     "Outubro", "Novembro","Dezembro"]
    nome_mes = meses[hoje.month-1] + " - " + str(hoje.year)
    semana = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
    
    # Para calcular quando começa e quando termina o calendário
    primeiro_dia = hoje - relativedelta(days = hoje.day-1)
    primeiro_dia_seguinte = primeiro_dia + relativedelta(months = 1)
    ultimo_dia = primeiro_dia_seguinte - relativedelta(days = 1)

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
    
    # Listagem de sala para o Select (pega todas as salas do banco de dados):
    primeira_data_reserva = datetime.combine(vetor_dias[0], datetime.min.time())
    ultima_data_reserva = datetime.combine(vetor_dias[-1], datetime.min.time())
    reservas = Reserva.objects.filter(
        data_reserva__range = [primeira_data_reserva, ultima_data_reserva],
        aprovacao = True,
    )
    
    calendario = []
    for dia in vetor_dias:
        reservas_dia=reservas.filter(data_reserva=dia)
        ativo = dia.month == mes and dia.weekday != 5 and dia.weekday != 6 and dia >= hoje
        data  = {'dia':dia, 'reservas':reservas_dia, 'ativo':ativo,}
        calendario.append(data)
    
    # Retorno na tela
    return render(request, 'djreservas/calendario.html', {
        'form': form, 
        'salas': salas, 
        'email': request.user.email,
        'nome_mes': nome_mes, 
        'semana': semana, 
        'mes': mes, 
        'hoje': hoje,
        'calendario': calendario,
    })