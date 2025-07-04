class Viagem:
    def __init__(self):
        self._dias_viag = ['Segunda', 'Quarta', 'Sexta']
        self._tempo_viag = 5
        self._linha = 'Picos à Teresina'
        self._horarios = {'Saída': '00:00', 'Chegada': '05:00'}
        self._preco = 100.0
    
    def mostra_viagens(self):
        print(f'{"Viagens disponíveis":^25}')
        print('-' * 30)
        for dias in self._dias_viag:
            print(f'|{dias:^25}')
            print(f'| Tempo de viagem: {self._tempo_viag} horas')
            print(f'| {"--> Horário <--":^10}')

            for situacao, hora in self._horarios.items():
                print(f'| {situacao}: {hora}')
            print(f'| Preço: R${self._preco:.2f}')
            print('-' * 30)

class Onibus:
    def __init__(self):
        self._poltronas = {'Segunda': list(range(1, 11)), 'Quarta': list(range(1, 11)), 'Sexta': list(range(1, 11))}