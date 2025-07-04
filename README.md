# Expresso Tour

## Descrição do Projeto

O **Expresso Tour** é um sistema desenvolvido como atividade para a disciplina de Programação Orientada a Objetos 2 (POO2). O objetivo é criar uma aplicação para **gerenciamento de vendas de passagens de ônibus** entre as cidades de Picos e Teresina, com recursos de cadastro de clientes, histórico de viagens, consulta de horários e gerenciamento de poltronas. O projeto utiliza os principais conceitos de POO, como herança, encapsulamento, abstração e polimorfismo.

## Objetivos

- Facilitar a venda de passagens entre Picos e Teresina.
- Permitir o cadastro seguro de clientes.
- Gerenciar o histórico de viagens e as passagens compradas.
- Oferecer consulta de horários e controle de poltronas disponíveis.
- Proporcionar praticidade e segurança para usuários e administradores do sistema.

## Tecnologias e Conceitos

- **Linguagem:** Python
- **Paradigma:** Programação Orientada a Objetos (POO)
- **Principais conceitos utilizados:**
  - **Herança:** Classes genéricas como base para classes específicas.
  - **Encapsulamento:** Proteção dos atributos das classes.
  - **Abstração:** Modelagem dos conceitos centrais do sistema.
  - **Polimorfismo:** Operações que podem ter implementações diferentes em subclasses.

## Estrutura de Classes

### Pessoa *(Classe Abstrata)*

- **Atributos:**
  - `nome: str`
  - `cpf: str`
  - `nasc: str`
- **Métodos:**
  - `get_nome()`
  - `get_cpf()`
  - `get_nasc()`

### Cadastro_Cliente *(Herda de Pessoa)*

- **Atributos:**
  - `senha: str`
- **Métodos:**
  - `get_senha()`
  - `set_senha(senha_nova)`
  - `login(user, senha)`

### Passagem

- **Atributos:**
  - `data_ida: str`
  - `hora_ida: str`
  - `origem: str`
  - `destino: str`
  - `valor: float`
- **Método:**
  - `exibe_passagem(nome, cpf)`

### ExpressoTour

- **Atributos:**
  - `cadastros: dict`
  - `passagens: dict`
  - `clientes_comp: dict`
- **Métodos:**
  - `op_cadastra_cliente(nome, cpf, nasc, senha)`
  - `op_efetua_login(cpf, senha)`
  - `op_compra_passagem(cpf, nome, origem, destino, poltrona, dia, tipo_pag)`
  - `op_cancela_passagem(cpf, id_passagem)`

## Como Executar

1. Clone ou baixe o repositório do projeto.
2. Execute o arquivo principal (ex: `main.py`).
3. Siga as instruções na interface do sistema para cadastrar clientes, comprar passagens, consultar histórico, etc.

## Equipe

- Arthur Sabino
- Luiz Nelson
- Mislayne Oliveira
- Rayssa Alves
- Vandirleya Barbosa
