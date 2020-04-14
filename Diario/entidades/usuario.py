class Usuario():

    def __init__(self,
         empreUserRazao,
         password,
         empreUserCNPJ,
         empreUserRespon,
         empreUserContato,
         empreUserEmail,
         endRua,
         endNum,
         endCEP,
         endCidade,
         endEstado):

        self.__empreUserRazao = empreUserRazao
        self.__password = password
        self.__empreUserCNPJ = empreUserCNPJ
        self.__empreUserRespon = empreUserRespon
        self.__empreUserContato = empreUserContato
        self.__empreUserEmail = empreUserEmail
        self.__endRua = endRua
        self.__endNum = endNum
        self.__endCEP = endCEP
        self.__endCidade = endCidade
        self.__endEstado = endEstado

####################################################
    @property
    def empreUserRazao(self):
        return self.__empreUserRazao
    @empreUserRazao.setter
    def empreUserRazao(self, empreUserRazao):
        self.__empreUserRazao = empreUserRazao
####################################################
    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password
####################################################
    @property
    def empreUserCNPJ(self):
        return self.__empreUserCNPJ
    @empreUserCNPJ.setter
    def empreUserCNPJ(self, empreUserCNPJ):
        self.__empreUserCNPJ = empreUserCNPJ
##################################################
    @property
    def empreUserRespon(self):
        return self.__empreUserRespon
    @empreUserRespon.setter
    def empreUserRespon(self, empreUserRespon):
        self.__empreUserRespon = empreUserRespon
##################################################
    @property
    def empreUserContato(self):
        return self.__empreUserContato
    @empreUserContato.setter
    def empreUserContato(self, empreUserContato):
        self.__empreUserContato = empreUserContato
###################################################
    @property
    def empreUserEmail(self):
        return self.__empreUserEmail
    @empreUserEmail.setter
    def empreUserEmail(self, empreUserEmail):
        self.__empreUserEmail = empreUserEmail
##################################################
    @property
    def endRua(self):
        return self.__endRua
    @endRua.setter
    def endRua(self, endRua):
        self.__endRua = endRua
####################################################
    @property
    def endNum(self):
        return self.__endNum
    @endNum.setter
    def endNum(self, endNum):
        self.__endNum = endNum
#####################################################
    @property
    def endCEP(self):
        return self.__endCEP
    @endCEP.setter
    def endCEP(self, endCEP):
        self.__endCEP = endCEP
#####################################################
    @property
    def endCidade(self):
        return self.__endCidade
    @endCidade.setter
    def endCidade(self, endCidade):
        self.__endCidade = endCidade
####################################################
    @property
    def endEstado(self):
        return self.__endEstado
    @endEstado.setter
    def endEstado(self, endEstado):
        self.__endEstado = endEstado
####################################################