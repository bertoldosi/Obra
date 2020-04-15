from datetime import date
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from Diario.forms import *
from Diario.models import *
from Diario.entidades.usuario import Usuario
from Diario.services import usuario_service


def index(request):
    usuario = request.user
    obra = Obras.objects.all()
    return render(request, 'Diario/00_index.html', locals())

def deslogar(request):
    logout(request)
    return redirect('logar')

def Logar(request):

    if request.method == "POST":
        form_login = LoginForm(data=request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('index')
        else:
            form_login = AuthenticationForm()
    else:
        form_login = AuthenticationForm()
    return render(request, 'Diario/0_logar.html', locals())





def CadUser(request):

    if request.method == 'POST':
        formuser = UsuarioForm(data=request.POST)

        if formuser.is_valid():
            empreUserRazao = formuser.cleaned_data['empreUserRazao']
            empreUserCNPJ = formuser.cleaned_data['empreUserCNPJ']
            empreUserRespon = formuser.cleaned_data['empreUserRespon']
            empreUserContato = formuser.cleaned_data['empreUserContato']
            empreUserEmail = formuser.cleaned_data['empreUserEmail']
            endRua = formuser.cleaned_data['endRua']
            endNum = formuser.cleaned_data['endNum']
            endCEP = formuser.cleaned_data['endCEP']
            endCidade = formuser.cleaned_data['endCidade']
            endEstado = formuser.cleaned_data['endEstado']
            password = formuser.cleaned_data['password1']

            usuario_novo = Usuario(empreUserRazao=empreUserRazao,
                                     empreUserCNPJ=empreUserCNPJ,
                                     empreUserRespon=empreUserRespon,
                                     empreUserContato=empreUserContato,
                                     empreUserEmail=empreUserEmail,
                                     endRua=endRua,
                                     endNum=endNum,
                                     endCEP=endCEP,
                                     endCidade=endCidade,
                                     endEstado=endEstado,
                                     password=password)

            usuario_service.cadastrar_usuario(usuario_novo)
            return redirect('logar')
        else:
            formuser = UsuarioForm()
    return render(request, 'Diario/0_cadUser.html', locals())

def RecupSenha(request):
    return render(request, 'Diario/0_RecupSenha.html', locals())

#------------DIARIO OBRA------------------------------------------------------------------------------------------------
def cadObra(request, idCliente):
    usuario = EmpresaUser.objects.get(id=1)
    clientes = EmpresaCliente.objects.all()
    cliente = EmpresaCliente.objects.get(id=idCliente)
    usuario = request.user
    formObra = FormObras()
    if request.method == 'POST':
        formObra = FormObras(request.POST)
        if formObra.is_valid():
            formObra.save()
            return redirect('index')
        else:
            HttpResponse('Formulario invalido!')
    else:
        HttpResponse('Post incorreto!')

    return render(request, 'Diario/01_cadObra.html', locals())

def SelecCliente(request):
    clientes = EmpresaCliente.objects.all()

    return render(request, 'Diario/14_SelecCliente.html', locals())

def cadDiario(request, idObra):
    obra = Obras.objects.get(id=idObra)
    diario = Diario.objects.filter(chave_obra=idObra)

    prazo = obra.obraPrazContrat


    saldo = prazo-date.today()

    #//////////////////////////////////////////
    lista = [0]
    for i in diario:                            #PEGANDO UM ID FICTICIO PARA ESSE DIARIO
        lista.append(i.id)
    id = max(lista, key=int)+1
    #//////////////////////////////////////////

    data = date.today()

    form = FormDiario()
    if request.method == 'POST':
        form = FormDiario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadMaoObraDir', id, 0)
        else:
            HttpResponse('Formulario invalido!')
    else:
        HttpResponse('Post incorreto!')
    return render(request, 'Diario/02_CadDiario.html', locals())



def cadMaoObraDir(request, idDiario, qtdMaoObraDir):
    maoObraDir = MaoObrasDiretas.objects.filter(diario=idDiario)

    ##############################################
    listaValue = []
    for i in maoObraDir:                            #somando a qtd de mão de obra
        listaValue.append(int(i.maoObraDirQtd))
    qtdMaoObraDir = sum(listaValue)
    ##############################################
    diario = Diario.objects.get(id=idDiario)
    ###

    form = FormMaoObrasDiretas()
    if request.method == 'POST':
        form = FormMaoObrasDiretas(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadMaoObraDir', idDiario, qtdMaoObraDir)
        else:
            HttpResponse('Formulario invalido!')
    else:
        HttpResponse('Post incorreto!')
    return render(request, 'Diario/03_CadMaoObraDir.html', locals())



def cadMaoObraInd(request, idDiario, qtdMaoObraDir, qtdMaoObraInd):
    maoObraInd = MaoObrasIndiretas.objects.filter(diario=idDiario)

    ##############################################
    listaValue = []
    for i in maoObraInd:  # somando a qtd de mão de obra
        listaValue.append(int(i.maoObraIndQtd))
    qtdMaoObraInd = sum(listaValue)
    ##############################################

    diario = Diario.objects.get(id=idDiario)
    form = FormMaoObrasIndiretas()
    if request.method == 'POST':
        form = FormMaoObrasIndiretas(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadMaoObraInd', idDiario, qtdMaoObraDir, qtdMaoObraInd)
        else:
            HttpResponse('Formulario invalido!')
    else:
        HttpResponse('Post incorreto!')
    return render(request, 'Diario/04_CadMaoObraInd.html', locals())


def cadEquipamento(request, idDiario, qtdMaoObraDir, qtdMaoObraInd, qtdEquipamento):

    equipamento = Equipamentos.objects.filter(diario=idDiario)
    ##############################################
    listaValue = []
    for i in equipamento:  # somando a qtd de mão de obra
        listaValue.append(int(i.EquipQtd))
    qtdEquipamento = sum(listaValue)
    ##############################################

    diario = Diario.objects.get(id=idDiario)
    formEquipamentos = FormEquipamentos()

    form = FormEquipamentos()
    if request.method == 'POST':
        form = FormEquipamentos(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadEquipamento', idDiario, qtdMaoObraDir, qtdMaoObraInd, qtdEquipamento)
        else:
            HttpResponse('Formulario invalido!')
    else:
        HttpResponse('Post incorreto!')
    return render(request, 'Diario/05_CadEquipamento.html', locals())


def cadEmpreitMaoObra(request, idDiario, qtdMaoObraDir, qtdMaoObraInd, qtdEquipamento, qtdEmpMaoObra):

    empreitMaoObra = EmpreiteirasMaoObras.objects.filter(diario=idDiario)

#------------
    listaValue = []
    for i in empreitMaoObra:  # somando a qtd de mão de obra
        listaValue.append(int(i.empMaoObraQtd))
    qtdEmpMaoObra = sum(listaValue)
    ##############################################

    diario = Diario.objects.get(id=idDiario)
    form = FormEmpreiteirasMaoObras()
    if request.method == 'POST':
        form = FormEmpreiteirasMaoObras(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadEmpreitMaoObra', idDiario, qtdMaoObraDir, qtdMaoObraInd, qtdEquipamento, qtdEmpMaoObra )
        else:
            HttpResponse('Formulario invalido!')
    else:
        HttpResponse('Post incorreto!')
    return render(request, 'Diario/06_CadEmpreitMaoObra.html', locals())


def cadEmpreitEquipamento(request, idDiario ,qtdMaoObraDir, qtdMaoObraInd, qtdEquipamento, qtdEmpMaoObra, qtdEmpEquipamento):
    empreitEquipamento = EmpreiteirasEquipamentos.objects.filter(diario=idDiario)

#---CALCULANDO TOTAL DE EQUIPAMENTOS DE EMPREITEIRAS------------------------------------------------
    listaValue = []
    for i in empreitEquipamento:  # somando a qtd de mão de obra
        listaValue.append(int(i.empEquipQtd))
    qtdEmpEquipamento = sum(listaValue)
#--------------------------------------------------------------------------------------------------

#---SOMANDO VALORES DOS SERVIÇOS---------------------------------------------------------------------
    qtdMaoObraDir = int(qtdMaoObraDir)
    qtdMaoObraInd = int(qtdMaoObraInd)
    qtdEmpMaoObra = int(qtdEmpMaoObra)

    qtdEquipamento = int(qtdEquipamento)
    qtdEmpEquipamento = int(qtdEmpEquipamento)

    qtdTotalMaoObra = int(qtdMaoObraDir+qtdMaoObraInd+qtdEmpMaoObra)
    qtdTotalEquipamento = int(qtdEquipamento+qtdEmpEquipamento)
#----------------------------------------------------------------------------------------------------

    diario = Diario.objects.get(id=idDiario)
    form = FormEmpreiteirasEquipamentos()
    if request.method == 'POST':
        form = FormEmpreiteirasEquipamentos(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadEmpreitEquipamento', idDiario, qtdMaoObraDir, qtdMaoObraInd, qtdEquipamento, qtdEmpMaoObra, qtdEmpEquipamento)
        else:
            HttpResponse('Formulario invalido!')
    else:
        HttpResponse('Post incorreto!')
    return render(request, 'Diario/07_CadEmpreitEquipamento.html', locals())


def cadClima(request, idDiario, qtdTotalMaoObra, qtdTotalEquipamento):
    clima = Clima.objects.filter(diario=idDiario)

    qtdTotalMaoObra = qtdTotalMaoObra
    qtdTotalEquipamento = qtdTotalEquipamento

    diario = Diario.objects.get(id=idDiario)
    formClima = FormClima()
    if request.method == 'POST':
        form = FormClima(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadClima', idDiario, qtdTotalMaoObra, qtdTotalEquipamento)
        else:
            HttpResponse('Formulario invalido!')
    else:
        HttpResponse('Post incorreto!')
    return render(request, 'Diario/08_CadClima.html', locals())


def cadObservacao(request, idDiario, qtdTotalMaoObra, qtdTotalEquipamento):
    observacao = Observacoes.objects.filter(diario=idDiario)

    qtdTotalMaoObra = qtdTotalMaoObra
    qtdTotalEquipamento = qtdTotalEquipamento

    diario = Diario.objects.get(id=idDiario)
    formObservacoes = FormObservacao()
    if request.method == 'POST':
        form = FormObservacao(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadObservacao', idDiario, qtdTotalMaoObra, qtdTotalEquipamento)
        else:
            HttpResponse('Formulario invalido!')
    else:
        HttpResponse('Post incorreto!')
    return render(request, 'Diario/09_CadObservacao.html', locals())


def MostraTotalServ(request, idDiario, qtdTotalMaoObra, qtdTotalEquipamento):
    totalServ = Observacoes.objects.filter(diario=idDiario)

    qtdTotalMaoObra = qtdTotalMaoObra
    qtdTotalEquipamento = qtdTotalEquipamento

    diario = Diario.objects.get(id=idDiario)
    form = FormQtdServ()
    if request.method == 'POST':
        form = FormQtdServ(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            HttpResponse('Formulario invalido!')
    else:
        HttpResponse('Post incorreto!')
    return render(request, 'Diario/10_MostraTotalServ.html', locals())


#############################################################################################

def Add_MaoObraDir(request, idDiario):

    diario = Diario.objects.get(id=idDiario)
    form = FormQtdServ()

    if request.method == 'POST':
        form = FormQtdServ(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadMaoObraDir')
        else:
            HttpResponse('Formulario invalido!')
    else:
        HttpResponse('Post incorreto!')
    return render(request, 'Diario/03_CadMaoObraDir.html', locals())

#---------------------------CLIENTE-----------------------------------------------------------------------------
def CadCliente(request):
    engenheiro = request.user
    clientes = EmpresaCliente.objects.filter(engenheiro=engenheiro)
    formCliente = FormEmpresaCliente()
    if request.method == 'POST':
        formCliente = FormEmpresaCliente(request.POST)
        if formCliente.is_valid():
            formCliente.save()
            return redirect('cadCliente')
        else:
            HttpResponse('Formulario invalido!')
    else:
        HttpResponse('Post incorreto!')
    return render(request, 'Diario/11_CadCliente.html', locals())

def MostrarCliente(request, idCliente):
    cliente = EmpresaCliente.objects.get(id=idCliente)
    return render(request, 'Diario/12_MostrarCliente.html', locals())

def EditarCliente(request, idCliente):
    cliente = EmpresaCliente.objects.get(id=idCliente)

    form = FormEmpresaCliente(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect(reverse_lazy('cadCliente'))
    return render(request, 'Diario/13_EditarCliente.html', locals())
