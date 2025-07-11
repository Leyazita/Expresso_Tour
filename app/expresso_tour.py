from cliente import Cliente
from passagem import Passagem
from viagem import Onibus, Viagem
from datetime import datetime, timedelta

def converter_dia_para_data_string(dia_semana_nome):
        dias_semana = {
            'Segunda': 0,
            'Quarta': 2,
            'Sexta': 4
        }
        hoje = datetime.now()
        alvo = dias_semana.get(dia_semana_nome)

        if alvo is None:
            raise ValueError("Dia inválido!")

        delta_dias = (alvo - hoje.weekday()) % 7
        if delta_dias == 0:
            delta_dias = 7  # Garante sempre a próxima ocorrência, não hoje

        data = hoje + timedelta(days=delta_dias)
        return data.strftime('%Y-%m-%d')

class ExpressoTour:
    def __init__(self):
        self.onibus = Onibus()
        self.viagem = Viagem(dia_semana='Segunda')

    def op_cadastra_cliente(self, nome, cpf, nasc, senha):
        if not Cliente.buscar_por_cpf(cpf):
            cliente = Cliente(cpf, nome, nasc, senha)
            cliente.salvar()
            return True, 'Cadastro efetuado com sucesso!'
        return False, f'ERRO! O CPF {cpf} já está cadastrado!'

    def op_efetua_login(self, cpf, senha):
        if Cliente.autenticar(cpf, senha):
            return True, 'Login efetuado com sucesso!'
        return False, 'CPF ou senha incorretos.'

    def op_verifica_senha(self, cpf, senha):
        return Cliente.autenticar(cpf, senha)

    def op_altera_senha(self, cpf, senha_nova):
        cliente = Cliente.buscar_por_cpf(cpf)
        if cliente:
            cliente.alterar_senha(senha_nova)
            return True, 'Senha alterada com sucesso!'
        return False, 'Cliente não encontrado.'
    
    def op_altera_nome(self, cpf, nome_novo):
        cliente = Cliente.buscar_por_cpf(cpf)
        if cliente:
            cliente.alterar_nome(nome_novo)
            return True, 'Nome alterado com sucesso!'
        return False, 'Cliente não encontrado.'

    def op_altera_cpf(self, cpf_atual, cpf_novo):
        cliente = Cliente.buscar_por_cpf(cpf_atual)
        if cliente:
            # Verifica se o novo CPF já está cadastrado
            if Cliente.buscar_por_cpf(cpf_novo):
                return False, '⚠️ CPF já cadastrado.'
            cliente.alterar_cpf(cpf_novo)
            return True, 'CPF alterado com sucesso!'
        return False, 'Cliente não encontrado.'


    def op_verifica_viagens(self):
        viagens = Viagem.listar()
        for v in viagens:
            print(f'| Dia: {v[0]} | Saída: {v[1]} | Chegada: {v[2]} | Tempo: {v[3]}h | Preço: R${v[4]:.2f}')

    def op_verifica_dia(self, dia):
        dias = {1: 'Segunda', 2: 'Quarta', 3: 'Sexta'}
        if isinstance(dia, str):
            return dia.capitalize() if dia.capitalize() in dias.values() else False
        return dias.get(dia, False)

    def op_exibe_poltronas(self, dia):
        dia_s = self.op_verifica_dia(dia)
        if not dia_s:
            return False, 'Dia inválido.'

        ocupadas = [p[0] for p in Onibus.listar_poltronas_ocupadas(dia_s) if p[1]]
        print('*' * 50)
        print(f'{"POLTRONAS":^50}')
        print('*' * 50)
        print('[X] -> Poltrona Preenchida')
        print('[Nº] -> Poltrona Vazia')
        print('-'*39)
        print('|', end=' ')
        for i in range(1, 11):
            simbolo = 'X' if i in ocupadas else str(i)
            print(f'{simbolo:<7}', end='')
            if i == 5:
                print('|\n|', end=' ')
            if i == 10:
                print('|\n' + '-'*39)
        return True, 'Exibição de poltronas concluída.'
    

    def op_compra_passagem(self, cpf, nome, origem, destino, poltrona, dia, tipo_pag):
        dia_s = self.op_verifica_dia(dia)
        if not dia_s:
            return False, 'Dia inválido.'

        tipo_pag_map = {1: 'Cartão', 2: 'Dinheiro', 3: 'Pix'}
        tipo_pag = tipo_pag_map.get(tipo_pag, None)
        if not tipo_pag:
            return False, 'Tipo de pagamento inválido.'

        if origem == 1 and destino == 2:
            origem, destino = 'Picos', 'Teresina'
        elif origem == 2 and destino == 1:
            origem, destino = 'Teresina', 'Picos'
        else:
            return False, 'Origem/destino inválidos.'

        ocupadas = [p[0] for p in Onibus.listar_poltronas_ocupadas(dia_s) if p[1]]
        if poltrona in ocupadas:
            return False, 'Poltrona já ocupada.'
        data_ida = converter_dia_para_data_string(dia_s)  # Função que transforma 'Segunda' em '2025-07-14' por exemplo
        passagem = Passagem(cpf, data_ida, '00:00', origem, destino, 100.0, tipo_pag, poltrona)

        # passagem = Passagem(cpf, dia_s, '00:00', origem, destino, 100.0, tipo_pag, poltrona)
        passagem.salvar()
        Onibus.ocupar_poltrona(dia_s, poltrona)
        passagem.exibe_passagem(nome)
        return True, 'Passagem comprada com sucesso!'

    def op_cancela_passagem(self, cpf, id_passagem):
        try:
            Passagem.cancelar(cpf, id_passagem)
            return True, 'Passagem cancelada com sucesso!'
        except:
            return False, 'Erro! PASSAGEM NÃO ENCONTRADA!'

    def op_verifica_passagens(self, cpf):
        try:
            passagens = Passagem.buscar_por_cpf(cpf)
            if passagens:
                for p in passagens:
                    print(p)
                return True, 'Passagens encontradas.'
            return False, 'Nenhuma passagem encontrada.'
        except:
            return False, 'Erro ao consultar passagens.'

    def op_consulta_nome_cli(self, cpf):
        cliente = Cliente.buscar_por_cpf(cpf)
        return cliente.nome if cliente else None
    
    

    

