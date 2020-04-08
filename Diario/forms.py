from django import forms
from Diario.models import *


class FormObras(forms.ModelForm):
    class Meta:
        model = Obras
        fields = '__all__'

class FormDiario(forms.ModelForm):
    class Meta:
        model = Diario
        fields = '__all__'


class FormEmpresaUser(forms.ModelForm):
    class Meta:
        model = EmpresaUser
        fields = '__all__'

class FormEmpreiteirasEquipamentos(forms.ModelForm):
    class Meta:
        model = EmpreiteirasEquipamentos
        fields = '__all__'

class FormEquipamentos(forms.ModelForm):
    class Meta:
        model = Equipamentos
        fields = '__all__'

class FormEmpreiteirasMaoObras(forms.ModelForm):
    class Meta:
        model = EmpreiteirasMaoObras
        fields = '__all__'

class FormMaoObrasIndiretas(forms.ModelForm):
    class Meta:
        model = MaoObrasIndiretas
        fields = '__all__'

class FormMaoObrasDiretas(forms.ModelForm):
    class Meta:
        model = MaoObrasDiretas
        fields = '__all__'

class FormClima(forms.ModelForm):
    class Meta:
        model = Clima
        fields = '__all__'

class FormObservacao(forms.ModelForm):
    class Meta:
        model = Observacoes
        fields = '__all__'

class FormQtdServ(forms.ModelForm):
    class Meta:
        model = QtdServ
        fields = '__all__'

#---------------------------------------------------

class FormEmpresaCliente(forms.ModelForm):
    class Meta:
        model = EmpresaCliente
        fields = '__all__'
