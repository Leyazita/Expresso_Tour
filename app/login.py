from abc import ABC, abstractmethod

class Login(ABC):

    @abstractmethod
    def login(self, user, senha):
        # efetua login
        pass

class Manipula_Login:

    def efetua_login(self, objeto, user, senha):

        if isinstance(objeto, Login):
            return objeto.login(user, senha)
        else:
            return False