from expresso_tour import ExpressoTour
import os
from time import sleep

def menu_principal():
    print('-'*50)
    print(f'|{"Expresso Tour - [Picos à Teresina]":^48}|')
    print('-'*50)

    print('| [1] - Efetuar Cadastro', end=f'{"|":>26}\n')
    print('| [2] - Fazer Login', end=f'{"|":>31}\n')
    print('| [3] - Verificar Viagens Disponíveis', end=f'{"|":>13}\n')
    print('| [4] - Comprar Passagem', end=f'{"|":>26}\n')
    print('| [5] - Verificar Vagas Em Uma Viagem', end=f'{"|":>13}\n')
    print('| [6] - Cancelar Passagem', end=f'{"|":>25}\n')
    print('| [0] - Sair', end=f'{"|":>38}\n')
    print('-'*50)

def barra_div():
    print('-'*50)

def op_cadastro_cliente():
    nome = str(input('Digite seu nome: ')).strip()
    cpf = str(input('Digite seu CPF (somente números e sem espaços!): ')).strip()
    barra_div()
    dia = str(input('Dia de nascimento: '))
    mes = str(input('Mês de nascimento: '))
    ano = str(input('Ano de nascimento: '))

    nasc = dia + '/' + mes + '/' + ano

    barra_div()
    print('Agora preencha uma senha para login no sistema!')
    barra_div()

    senha = str(input('-> Senha*: ')).strip()

    barra_div()
    return expresso.op_cadastra_cliente(nome, cpf, nasc, senha)
        
def op_fazer_login():
    print('|', '-' * 38, '|')
    print('|', f'{f"MENU DE LOGIN":^38}', '|')
    print('|', '-' * 38, '|')
    
    usuario = str(input('| CPF*: ')).strip()
    senha = str(input('| Senha*: ')).strip()

    nome = expresso.op_consulta_nome_cli(usuario)
    barra_div()
    return (expresso.op_efetua_login(usuario, senha)), (nome, usuario)
        
def op_verificar_viagens_disp():
    expresso.op_verifica_viagens()

def op_comprar_passagem():
    op_verificar_viagens_disp()

    print(f'|Escolha o dia da viagem:\n|[1] - Segunda\n|[2] - Quarta\n|[3] - Sexta\n{"-" * 30}')
    resp = int(input('|Digite aqui -> '))
    
    expresso.op_exibe_poltronas(resp)

    barra_div()
    print(f'{"|Agora preencha os dados para compra da passagem: "}')
    barra_div()

    polt = int(input('|Escolha sua poltrona*: '))
    cpf = str(input('|Informe seu CPF*: ')).strip()
    nome = str(input('|Nome completo*: ')).strip()
    origem = int(input('|ORIGEM -> [1] - Picos --- [2] - Teresina|: '))
    destino = int(input('|DESTINO -> [1] - Picos --- [2] - Teresina|: '))
    tipo_pag = int(input('|Tipo de pagamento -> [1] - Cartão -- [2] - Dinheiro -- [3] - Pix|: '))
    barra_div()

    
    return expresso.op_compra_passagem(cpf, nome, origem, destino, polt, resp, tipo_pag)
    '''except:
        return False, 'Falha na operação!'''

def op_verificar_vagas_onibus():
    op_verificar_viagens_disp()

    print(f'|Escolha o dia que deseja ver as vagas:\n|[1] - Segunda\n|[2] - Quarta\n|[3] - Sexta\n{"-" * 30}')
    dia = int(input('|Digite aqui -> '))
    print('Procurando vagas...')
    sleep(1.5)
    

    return expresso.op_exibe_poltronas(dia)

def op_cancelar_passagem():
    cpf = str(input('|Informe o seu cpf para verificar suas passagens compradas: ')).strip()
    barra_div()

    situacao, mensagem = expresso.op_verifica_passagens(cpf)

    if situacao == False:
        return situacao, mensagem
    else:
        print(f'{mensagem:^40}')
        print('|', '-' * 38, '|')
        id = int(input('|Digite o ID da passagem a ser cancelada: '))
        print('-' * 40)

        situacao, mensagem = expresso.op_cancela_passagem(cpf, id)
        return situacao, mensagem

def op_verifica_passagens_cli(cpf):
    return expresso.op_verifica_passagens(cpf)

def op_altera_senha(cpf):
    senha_atual = str(input('Digite sua senha atual: ')).strip()
    
    if expresso.op_verifica_senha(cpf, senha_atual):

        senha_nova = str(input('Digite a nova senha: ')).strip()
        
        barra_div()
        return expresso.op_altera_senha(cpf, senha_nova)
    else:
        return False, 'Senha incorreta!'

def menu_logado(nome):

    print(f'{f"Bem-vindo {nome}":^50}')
    print('-'*50)
    print(f'|{"Expresso Tour - [Picos à Teresina]":^48}|')
    print('-'*50)

    print('| [1] - Verificar Viagens Disponíveis', end=f'{"|":>13}\n')
    print('| [2] - Comprar Passagem', end=f'{"|":>26}\n')
    print('| [3] - Verificar Vagas Em Uma Viagem', end=f'{"|":>13}\n')
    print('| [4] - Cancelar Passagem', end=f'{"|":>25}\n')
    print('| [5] - Verificar minhas passagens', end=f'{"|":>16}\n')
    print('| [6] - Alterar senha da conta', end=f'{"|":>20}\n')
    print('| [0] - Deslogar', end=f'{"|":>34}\n')
    print('-'*50)

def cliente_logado(nome, cpf):

    while True:
        menu_logado(nome)
        op_cli = int(input('Digite sua opção: '))
        barra_div()

        if op_cli == 0:
            print('Deslogando...')
            sleep(1.5)
            
            break

        elif op_cli == 1:
            op_verificar_viagens_disp()
            sleep(2)
             

        elif op_cli == 2:
            _, mensagem = op_comprar_passagem()
            print(f'{mensagem:^40}')
            sleep(3.5)
            
            
        elif op_cli == 3:
            _, mensagem = op_verificar_vagas_onibus()
            print(mensagem)
            sleep(3)
            

        elif op_cli == 4:
            _, mensagem = op_cancelar_passagem()
            print(mensagem)
            sleep(2.5)
            

        elif op_cli == 5:
            _, mensagem = op_verifica_passagens_cli(cpf)
            print(mensagem)
            sleep(2.5)
            

        elif op_cli == 6:
            _, mensagem = op_altera_senha(cpf)
            print(mensagem)
            sleep(2.5)
            
        
        else:
            print('Valor inválido!')
            sleep(2.5)
            

expresso = ExpressoTour()
while True:
    menu_principal()
    op = int(input('Digite sua opção: '))
    barra_div()

    if op == 0:
        break

    elif op == 1:
        _, mensagem = op_cadastro_cliente()
        print(mensagem)
        sleep(2)
        
    
    elif op == 2:
        (situacao, mensagem), (nome, cpf) = op_fazer_login()
        print(mensagem)
        sleep(1.5)
        barra_div()
        

        if situacao == True:
            cliente_logado(nome, cpf)

    elif op == 3:
        op_verificar_viagens_disp()
        sleep(2)
          
    
    elif op == 4:
        _, mensagem = op_comprar_passagem()
        print(f'{mensagem:^40}')
        sleep(3.5)
        
    
    elif op == 5:
        _, mensagem = op_verificar_vagas_onibus()
        print(mensagem)
        sleep(3)
        

    elif op == 6:
        _, mensagem = op_cancelar_passagem()
        print(mensagem)
        sleep(2.5)
        

    else:
        print('Valor inválido!')
        sleep(2.5)
        