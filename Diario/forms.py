from django import forms
from django.contrib.auth.forms import AuthenticationForm

from Diario.models import *


########### usuario_form ################

class UsuarioForm(forms.ModelForm):
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma senha', widget=forms.PasswordInput)

    class Meta:
        model = EmpresaUser
        fields = ('empreUserRazao',
                  'empreUserCNPJ',
                  'empreUserEmail',
                  'empreUserRespon',
                  'empreUserContato',
                  'endRua',
                  'endNum',
                  'endCEP',
                  'endCidade',
                  'endEstado')

    # verificar se as duas senha são iguais
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('As senhas informadas não são iguais!')
        return password2

    # inserindo a senha no banco criptofrada
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set__password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    username = forms.EmailField()
    class Meta:
        model = EmpresaUser
        fields = ['username', 'password']



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


# ---------------------------------------------------

class FormEmpresaCliente(forms.ModelForm):
    class Meta:
        model = EmpresaCliente
        fields = '__all__'
