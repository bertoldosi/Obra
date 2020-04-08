from django.urls import path
from Diario.views import *

urlpatterns = [
    path('', index, name="index"),

    path('cadObra/<idCliente>', cadObra, name="cadObra"),
    path('selecCliente', SelecCliente, name="selecCliente"),
    path('cadDiario/<idObra>', cadDiario, name="cadDiario"),
    path('cadMaoObraDir/<idDiario>/<qtdMaoObraDir>', cadMaoObraDir, name="cadMaoObraDir"),
    path('cadMaoObraInd/<idDiario>/<qtdMaoObraDir>/<qtdMaoObraInd>', cadMaoObraInd, name="cadMaoObraInd"),
    path('cadEquipamento/<idDiario>/<qtdMaoObraDir>/<qtdMaoObraInd>/<qtdEquipamento>', cadEquipamento, name="cadEquipamento"),
    path('cadEmpreitMaoObra/<idDiario>/<qtdMaoObraDir>/<qtdMaoObraInd>/<qtdEquipamento>/<qtdEmpMaoObra>', cadEmpreitMaoObra, name="cadEmpreitMaoObra"),
    path('cadEmpreitEquipamento/<idDiario>/<qtdMaoObraDir>/<qtdMaoObraInd>/<qtdEquipamento>/<qtdEmpMaoObra>/<qtdEmpEquipamento>', cadEmpreitEquipamento, name="cadEmpreitEquipamento"),
    path('cadClima/<idDiario>/<qtdTotalMaoObra>/<qtdTotalEquipamento>', cadClima, name="cadClima"),
    path('cadObservacao/<idDiario>/<qtdTotalMaoObra>/<qtdTotalEquipamento>', cadObservacao, name="cadObservacao"),

    path('mostraTotalServ/<idDiario>/<qtdTotalMaoObra>/<qtdTotalEquipamento>', MostraTotalServ, name="mostraTotalServ"),
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    path('cadCliente', CadCliente, name="cadCliente"),
    path('mostrarCliente/<idCliente>', MostrarCliente, name="mostrarCliente"),
    path('editarCliente/<idCliente>', EditarCliente, name="editarCliente"),
]