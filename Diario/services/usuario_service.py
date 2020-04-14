from ..models import EmpresaUser

#meto create_user é especil do modulo AbstractBaseUser da model.
def cadastrar_usuario(usuario):
    usuario = EmpresaUser.objects.create_user(
                                         empreUserRazao=usuario.empreUserRazao,
                                         empreUserCNPJ=usuario.empreUserCNPJ,
                                         empreUserRespon=usuario.empreUserRespon,
                                         empreUserContato=usuario.empreUserContato,
                                         empreUserEmail=usuario.empreUserEmail,
                                         endRua=usuario.endRua,
                                         endNum=usuario.endNum,
                                         endCEP=usuario.endCEP,
                                         endCidade=usuario.endCidade,
                                         endEstado=usuario.endEstado,
                                         password=usuario.password)
    usuario.save()