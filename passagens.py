from random import randint

# Passagem Cliente
class Passagem:
    def __init__(self):
        self._data_ida = ''
        self._hora_ida = ''
        self._destino = ''
        self._origem = ''
        self._valor = 100.00
        self._id_passagem = randint(1,500)
        self._pagamento = ''
        self._poltrona = 0
    
    def exibe_passagem(self, nome, cpf):
        print('|', '-' * 38, '|')
        print(f'|{f"CARTÃO DE EMBARQUE":^40}|')
        print('|', '-' * 38, '|')

        print(f'| ID da passagem: {self._id_passagem}')
        print(f'| Nome do passageiro: {nome}')
        print(f'| Documento CPF: {cpf}')
        print(f'| Poltrona: {self._poltrona}')
        print(f'| Valor: R${self._valor:.2f}')
        print(f'| Tipo de pagamento: {self._pagamento}')
        print(f'| Origem: {self._origem}')
        print(f'| Destino: {self._destino}')
        print(f'| Data: {self._data_ida}-feira')
        print(f'| Hora de partida: {self._hora_ida}')
        print('|', '-' * 38, '|')