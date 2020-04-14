from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from .manager import UsuarioManager


class Obras(models.Model):
    obraNome = models.CharField('Nome ', max_length=30)
    obraPrazContrat = models.DateField('Prazo do Contrato(data)')
    empresaUser = models.ForeignKey('EmpresaUser', on_delete=models.CASCADE)
    empresaCliente = models.ForeignKey('EmpresaCliente', on_delete=models.CASCADE)

    def __str__(self):
        return self.obraNome


class EmpresaUser(AbstractBaseUser):
    objects = UsuarioManager()

    empreUserRazao = models.CharField('Nome da razão social', max_length=50)
    empreUserCNPJ = models.CharField('CNPJ', max_length=20)
    empreUserRespon = models.CharField('Responsável', max_length=50)
    empreUserContato = models.CharField('Contato', max_length=12)
    empreUserEmail = models.EmailField('Email', unique=True)
    endRua = models.CharField('Rua', max_length=50)
    endNum = models.IntegerField('Número')
    endCEP = models.CharField('CEP', max_length=50)
    endCidade = models.CharField('Cidade', max_length=50)
    endEstado = models.CharField('Estado', max_length=50)

    USERNAME_FIELD = 'empreUserEmail'

    REQUIRED_FIELDS = ['empreUserRazao',
                       'empreUserCNPJ',
                       'empreUserRespon',
                       'empreUserContato',
                       'endRua',
                       'endNum',
                       'endCEP',
                       'endCidade',
                       'endEstado'
                       ]

    def __str__(self):
        return self.empreUserRazao


class EmpresaCliente(models.Model):
    empClienteRazao = models.CharField('Nome da razão social', max_length=50)
    empClienteCNPJ = models.CharField('CNPJ', max_length=20)
    empClienteRespon = models.CharField('Responsável', max_length=50)
    empClienteContato = models.CharField('Contato', max_length=12)
    empClienteEmail = models.EmailField('Email')

    endRua = models.CharField('Rua', max_length=50)
    endNum = models.IntegerField('Número')
    endCEP = models.CharField('CEP', max_length=50)
    endCidade = models.CharField('Cidade', max_length=50)
    endEstado = models.CharField('Estado', max_length=50)

    def __str__(self):
        return self.empClienteRazao


class Diario(models.Model):
    diarioDtAtual = models.DateField('Data atual ')
    diarioNumDiario = models.IntegerField('Número do diário')
    diarioDiasTrab = models.IntegerField('Dias trabalhados')
    diarioSaldoPraz = models.IntegerField('Saldo de dias restantes')
    chave_obra = models.ForeignKey('Obras', on_delete=models.CASCADE)

    def __str__(self):
        numeroDoDiario = str(self.diarioNumDiario)
        return numeroDoDiario


class EmpreiteirasEquipamentos(models.Model):
    empEquipDesc = models.CharField('Descrição', max_length=50)
    empEquipQtd = models.IntegerField('Quantidade')
    diario = models.ForeignKey('Diario', on_delete=models.CASCADE)

    def __str__(self):
        return self.empEquipDesc


class Equipamentos(models.Model):
    EquipDesc = models.CharField('Descrição', max_length=50)
    EquipQtd = models.IntegerField('Quantidade')
    diario = models.ForeignKey('Diario', on_delete=models.CASCADE)

    def __str__(self):
        return self.EquipDesc


class EmpreiteirasMaoObras(models.Model):
    empMaoObraDesc = models.CharField('Descrição', max_length=50)
    empMaoObraQtd = models.IntegerField('Quantidade')
    diario = models.ForeignKey('Diario', on_delete=models.CASCADE)

    def __str__(self):
        return self.empMaoObraDesc


class MaoObrasIndiretas(models.Model):
    maoObraIndDesc = models.CharField('Descrião', max_length=50)
    maoObraIndQtd = models.IntegerField('Quantidade')
    diario = models.ForeignKey('Diario', on_delete=models.CASCADE)

    def __str__(self):
        return self.maoObraIndDesc


class MaoObrasDiretas(models.Model):
    maoObraDirDesc = models.CharField('Descrição', max_length=50)
    maoObraDirQtd = models.IntegerField('Quantidade')
    diario = models.ForeignKey('Diario', on_delete=models.CASCADE)

    def __str__(self):
        return self.maoObraDirDesc


class Clima(models.Model):
    climaManha = models.CharField('Condições do tempo manhã', max_length=20)
    climaTarde = models.CharField('Condições do tempo tarde', max_length=20)
    climaNoite = models.CharField('Condições do tempo noite', max_length=20)
    diario = models.ForeignKey('Diario', on_delete=models.CASCADE)

    def __str__(self):
        return self.climaManha


class Observacoes(models.Model):
    obsDescServ = models.TextField('Descrição dos Serviços')
    obsComentario = models.TextField('Comentário')
    diario = models.ForeignKey('Diario', on_delete=models.CASCADE)

    def __str__(self):
        return self.obsDescServ


class QtdServ(models.Model):
    QtdServMaoObra = models.IntegerField('Quantidade geral de Mão de Obras')
    QtdServEquip = models.IntegerField('Quantidade geral de Equipamentos')
    diario = models.ForeignKey('Diario', on_delete=models.CASCADE)

    def __str__(self):
        return self.QtdServEquip
