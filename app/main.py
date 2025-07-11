from expresso_tour import ExpressoTour
import os
from time import sleep

expresso = ExpressoTour()

def menu_principal():
    print('-'*50)
    print(f'|{"Expresso Tour - [Picos à Teresina]":^48}|')
    print('-'*50)
    print('| [1] - Efetuar Cadastro', end=f'{"|":>26}\n')
    print('| [2] - Fazer Login', end=f'{"|":>31}\n')
    print('| [0] - Sair', end=f'{"|":>38}\n')
    print('-'*50)

def barra_div():
    print('-'*50)

def op_cadastro_cliente():
    nome = input('Digite seu nome: ').strip()
    cpf = input('Digite seu CPF (somente números): ').strip()
    dia = input('Dia de nascimento: ')
    mes = input('Mês de nascimento: ')
    ano = input('Ano de nascimento: ')
    nasc = f"{ano}-{mes.zfill(2)}-{dia.zfill(2)}"
    senha = input('-> Senha*: ').strip()
    return expresso.op_cadastra_cliente(nome, cpf, nasc, senha)

def op_fazer_login():
    os.system('clear') or None
    print('|', '-' * 38, '|')
    print('|', f'{"MENU DE LOGIN":^38}', '|')
    print('|', '-' * 38, '|')
    usuario = input('| CPF*: ').strip()
    senha = input('| Senha*: ').strip()
    nome = expresso.op_consulta_nome_cli(usuario)
    return (expresso.op_efetua_login(usuario, senha)), (nome, usuario)

def cliente_logado(nome, cpf):
    while True:
        print(f'{f"Bem-vindo {nome}":^50}')
        print('-'*50)
        print('| [1] - Verificar Viagens Disponíveis', end=f'{"|":>13}\n')
        print('| [2] - Comprar Passagem', end=f'{"|":>26}\n')
        print('| [3] - Verificar Vagas Em Uma Viagem', end=f'{"|":>13}\n')
        print('| [4] - Cancelar Passagem', end=f'{"|":>25}\n')
        print('| [5] - Verificar minhas passagens', end=f'{"|":>16}\n')
        print('| [6] - Alterar senha da conta', end=f'{"|":>20}\n')
        print('| [7] - Alterar nome', end=f'{"|":>30}\n')
        print('| [8] - Alterar CPF', end=f'{"|":>32}\n')
        print('| [0] - Deslogar', end=f'{"|":>34}\n')
        print('-'*50)

        op = int(input('Digite sua opção: '))
        barra_div()

        if op == 0:
            print('Deslogando...')
            sleep(1.5)
            os.system('clear') or None
            break
        elif op == 1:
            expresso.op_verifica_viagens()
        elif op == 2:
            print('|Escolha o dia: [1] Segunda [2] Quarta [3] Sexta')
            dia = int(input('|Digite -> '))
            expresso.op_exibe_poltronas(dia)
            polt = int(input('|Poltrona*: '))
            origem = int(input('|Origem -> [1] Picos [2] Teresina: '))
            destino = int(input('|Destino -> [1] Picos [2] Teresina: '))
            tipo_pag = int(input('|Pagamento -> [1] Cartão [2] Dinheiro [3] Pix: '))
            _, msg = expresso.op_compra_passagem(cpf, nome, origem, destino, polt, dia, tipo_pag)
            print(msg)
        elif op == 3:
            dia = int(input('|Dia -> [1] Segunda [2] Quarta [3] Sexta: '))
            _, msg = expresso.op_exibe_poltronas(dia)
            print(msg)
        elif op == 4:
            id_pass = int(input('|ID da passagem para cancelar: '))
            _, msg = expresso.op_cancela_passagem(cpf, id_pass)
            print(msg)
        elif op == 5:
            _, msg = expresso.op_verifica_passagens(cpf)
            print(msg)
        elif op == 6:
            atual = input('|Senha atual: ')
            if expresso.op_verifica_senha(cpf, atual):
                nova = input('|Nova senha: ')
                _, msg = expresso.op_altera_senha(cpf, nova)
                print(msg)
            else:
                print('Senha incorreta!')
        if op == 7:
            novo_nome = input('|Novo nome: ').strip()
            _, msg = expresso.op_altera_nome(cpf, novo_nome)
            print(msg)
            if _:
                nome = novo_nome  # atualiza nome local

        elif op == 8:
            novo_cpf = input('|Novo CPF (somente números): ').strip()
            _, msg = expresso.op_altera_cpf(cpf, novo_cpf)
            print(msg)
            if _:
                cpf = novo_cpf  # atualiza cpf local
        sleep(2.5)
        os.system('clear') or None

while True:
    menu_principal()
    op = int(input('Digite sua opção: '))
    barra_div()

    if op == 0:
        break
    elif op == 1:
        _, msg = op_cadastro_cliente()
        print(msg)
    elif op == 2:
        (ok, msg), (nome, cpf) = op_fazer_login()
        print(msg)
        if ok:
            cliente_logado(nome, cpf)
    sleep(2.5)
    os.system('clear') or None
