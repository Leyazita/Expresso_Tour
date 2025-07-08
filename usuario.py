from abc import ABC
from passagens import Passagem
from historico_pass import HistoricoPass

class Pessoa(ABC):
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
    
    @property
    def get_nome(self):
        return self.__nome
    
    @property 
    def get_cpf(self):
        return self.__cpf

class Comprador(Pessoa):
    def __init__(self, nome, cpf):
        self._nome = nome
        self._cpf = cpf
        self._passagem = Passagem()

class Cadastro_Cliente(Pessoa):
    def __init__(self, nome, cpf, nasc, senha):
        super().__init__(nome, cpf)
        self._nasc = nasc
        self._senha = senha
        self.historico_pass = HistoricoPass()

    @property
    def get_senha(self):
        return self._senha
    
    @get_senha.setter
    def set_senha(self, senha_nova):
        
        if senha_nova != self.get_senha:
            self._senha = senha_nova
            return True
        else:
            return False

    def login(self, user, senha):

        if user == self.get_cpf and senha == self.get_senha:
            return True, 'Login efetuado com sucesso!'
        else:
            return False, 'ERRO! Senha incorreta!'