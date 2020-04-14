from django.contrib.auth.models import BaseUserManager


class UsuarioManager(BaseUserManager):
    def create_user(self, empreUserRazao,
                          empreUserEmail,
                          password,
                          empreUserCNPJ,
                          empreUserRespon,
                          empreUserContato,
                          endRua,
                          endNum,
                          endCEP,
                          endCidade,
                          endEstado):
        if not empreUserEmail:
            raise ValueError('O usuário precisa de um email!')

        usuario = self.model(
            empreUserRazao=empreUserRazao,
            empreUserEmail=self.normalize_email(empreUserEmail),
            password=password,
            empreUserCNPJ=empreUserCNPJ,
            empreUserRespon=empreUserRespon,
            empreUserContato=empreUserContato,
            endRua=endRua,
            endNum=endNum,
            endCEP=endCEP,
            endCidade=endCidade,
            endEstado=endEstado,
        )
        usuario.set_password(password)
        usuario.save()
        return usuario
