from usuario import Comprador, Cadastro_Cliente
from login import Manipula_Login, Login
from viagem import Onibus, Viagem

class ExpressoTour():

    def __init__(self):
        self._cadastros = {}
        self._passagens = {}
        self._clientes_comp = {}
        self.onibus = Onibus()
        self.viagem = Viagem()
    
    def op_verifica_cadastro(self, cpf): # verifica se o cpf está cadastrado no sistema
        
        if cpf in self._cadastros:
            return True
        else:
            return False

    def op_cadastra_cliente(self, nome, cpf, nasc, senha): # cadastra o cliente
        
        if (self.op_verifica_cadastro(cpf) == False):

            cadastro = Cadastro_Cliente(nome, cpf, nasc, senha)
            self._cadastros[cpf] = cadastro
            return True, 'Cadastro efetuado com sucesso!'
        else:
            return False, f'ERRO! O CPF {cpf} já está cadastrado!'
    
    def op_efetua_login(self, cpf, senha): # realiza login no sistema
        
        if self.op_verifica_cadastro(cpf) == True:
            
            Login.register(Cadastro_Cliente)
            login = Manipula_Login()
            _, mensagem = login.efetua_login(self._cadastros[cpf], cpf, senha)
            return True, mensagem
        else:
            return False, 'CPF não encontrado!'

    def op_verifica_senha(self, cpf, senha): # verifica se a senha do cadastro está correta
        
        if senha == self._cadastros[cpf].get_senha:
            return True
        else:
            return False

    def op_altera_senha(self, cpf, senha_nova): #altera a senha atual do cadastro
        
        try:
            self._cadastros[cpf].set_senha = senha_nova
            return True, 'Senha alterada com sucesso!'
        except:
            return False, 'Erro ao alterar a senha! Tente novamente...'

    def op_verifica_viagens(self): # verifica viagens disponíveis
        self.viagem.mostra_viagens()
    
    def op_verifica_dia(self, dia):     #verificar dia da semana correspondente a resposta do usuario

            if type(dia) == str or dia == 1:
                dia = 'Segunda'
                return dia
            elif type(dia) == str or dia == 2:
                dia = 'Quarta'
                return dia
            elif type(dia) == str or dia == 3:
                dia = 'Sexta'
                return dia
            else:
                return False

    def verifica_polt(self, polt, poltronas):  # verificar se a poltrona está vazia

        if poltronas[polt - 1] == 'X':
            return False, 'Poltrona Preenchida'
        else:
            return True, 'Ok'

    def op_exibe_poltronas(self, dia): # mostra poltronas do onibus de acordo com o dia escolhido

        dia_s = self.op_verifica_dia(dia)

        try:
            if type(dia_s) == str:
                poltronas = self.onibus._poltronas[dia_s]

                print('*' * 50)
                print(f'{"POLTRONAS":^50}')
                print('*' * 50)
                print('[X] -> Poltrona Preenchida')
                print('[N°] -> Poltrona Vazia')
                print('-'*39)
                print('|', end= ' ')
                for i, polt in enumerate(poltronas):
                    if i < 4:
                        print(f'{polt:<7}', end='')
                    elif i == 4:
                        print(f'{polt:<7} |\n')
                        print('|', end=' ')
                    elif i == 9:
                        print(f'{polt:<7} |\n')
                        print('-'*39)
                    else:
                        print(f'{polt:<7}', end='')
                return True, 'Poltronas disponíveis no momento!'
            else:
                return False, 'Dia da semana digitado errado! Tente novamente...'
        except:
            return False, 'Erro na operação!'

    def op_compra_passagem(self, cpf, nome, origem, destino, poltrona, dia, tipo_pag): # procedimentos para efetuação da compra
        
        dia_s = self.op_verifica_dia(dia)
        
        if type(dia_s) == str:

            if cpf in self._clientes_comp.keys() and nome.lower() != self._clientes_comp[cpf]._nome.lower():
                return False, 'Nome diferente do já correspondente ao CPF!'

            else:

                poltronas = self.onibus._poltronas[dia_s]


                situacao, mensagem = self.verifica_polt(poltrona, poltronas)

                if situacao == True:
                    
                    poltronas[poltrona - 1] = 'X'
                    self.onibus._poltronas[dia_s] = poltronas
                    
                    comprador = Comprador(nome, cpf)

                    comprador._passagem._data_ida = dia_s
                    comprador._passagem._hora_ida = self.viagem._horarios['Saída']
                    
                    if origem == 1 and destino == 2:
                        origem = 'Picos'
                        destino = 'Teresina'
                    elif origem == 2 and destino == 1:
                        origem = 'Teresina'
                        destino = 'Picos'
                    else:
                        return False, 'Origem e destino inseridos incorretamente!'
                    
                    if tipo_pag == 1:
                        tipo_pag = 'Cartão'
                    elif tipo_pag == 2:
                        tipo_pag = 'Dinheiro'
                    elif tipo_pag == 3:
                        tipo_pag = 'Pix'
                    else:
                        return False, 'Tipo de pagamento inválido!'
                    
                    comprador._passagem._origem = origem
                    comprador._passagem._destino = destino
                    comprador._passagem._pagamento = tipo_pag
                    comprador._passagem._poltrona = poltrona
                    self._clientes_comp[cpf] = comprador

                    self.op_cartao_embarque(cpf, comprador)

                    if self.op_verifica_cadastro(cpf):
                        self._cadastros[cpf].historico_pass.adiciona_passagem(comprador._passagem)

                    return True, 'Passagem comprada com sucesso!'
            
                else:
                    return situacao, mensagem

        else:
            return dia_s, 'Falha ao comprar passagem!'

    def op_cancela_passagem(self, cpf, id_passagem): # cancela passagem pelo id da passagem 
        
        if self.op_verifica_cadastro(cpf):
            passagens_to_check = self._cadastros[cpf].historico_pass.passagens
        elif cpf in self._passagens:
            passagens_to_check = self._passagens[cpf]
        else:
            return False, 'CPF não encontrado no sistema ou nenhuma passagem comprada!'

        for passagem in passagens_to_check:
            if passagem._id_passagem == id_passagem:
                
                
                dia_passagem = passagem._data_ida 
                poltrona_passagem = passagem._poltrona

                
                if dia_passagem in self.onibus._poltronas:
                    self.onibus._poltronas[dia_passagem][poltrona_passagem - 1] = poltrona_passagem
                
                passagens_to_check.remove(passagem)
                return True, 'Passagem cancelada com sucesso!'
        
        return False, 'Erro! PASSAGEM NÃO ENCONTRADA!' 

    def op_verifica_passagens(self, cpf): # verifica passagens compradas por cliente, caso tenha
        
        try:
            if self.op_verifica_cadastro(cpf):
                passagens_cad = self._cadastros[cpf].historico_pass.passagens
                
                for passagem in passagens_cad:
                    passagem.exibe_passagem(self._cadastros[cpf].get_nome, self._cadastros[cpf].get_cpf)

                return True, 'Passagens compradas!'

            elif cpf in self._passagens:
                compras_cli = self._passagens[cpf]
                
                for compra in compras_cli:
                    compra._passagem.exibe_passagem(compra._nome, compra._cpf)

                return True, 'Passagens compradas!'
            else:
                return False, 'Nenhuma passagem comprada!'
        except:
            return False, 'CPF não encontrado no sistema!'

    def op_consulta_nome_cli(self, cpf): # consulta nome do cliente pelo CPF
        
        if self.op_verifica_cadastro(cpf) == True:
            nome = self._cadastros[cpf].get_nome
            return nome
    
    def op_cartao_embarque(self, cpf, comprador): # emite e armazena cartão de embarque do comprador

        if len(self._passagens) == 0:
            self._passagens[cpf] = []
            self._passagens[cpf].append(comprador)
            
        else:
            if cpf not in self._passagens:
                self._passagens[cpf] = []
                self._passagens[cpf].append(comprador)

            else:
                self._passagens[cpf].append(comprador)
        
        comprador._passagem.exibe_passagem(comprador._nome, comprador._cpf)