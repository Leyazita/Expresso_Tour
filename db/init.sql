-- Tabela de clientes (Cadastro_Cliente herda de Pessoa)
CREATE TABLE IF NOT EXISTS cliente (
    cpf VARCHAR(14) PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    nascimento DATE NOT NULL,
    senha VARCHAR(100) NOT NULL
);

-- Tabela de passagens (objeto Passagem associado ao cliente/Comprador)
CREATE TABLE IF NOT EXISTS passagem (
    id SERIAL PRIMARY KEY,
    cpf_cliente VARCHAR(14) NOT NULL,
    data_ida DATE NOT NULL,
    hora_ida TIME NOT NULL,
    origem VARCHAR(50) NOT NULL,
    destino VARCHAR(50) NOT NULL,
    valor NUMERIC(10,2) NOT NULL DEFAULT 100.00,
    pagamento VARCHAR(20) NOT NULL,
    poltrona INT NOT NULL CHECK (poltrona BETWEEN 1 AND 10),
    FOREIGN KEY (cpf_cliente) REFERENCES cliente(cpf) ON DELETE CASCADE
);

-- Tabela de viagens (equivalente à classe Viagem)
CREATE TABLE IF NOT EXISTS viagem (
    id SERIAL PRIMARY KEY,
    dia_semana VARCHAR(10) CHECK (dia_semana IN ('Segunda', 'Quarta', 'Sexta')),
    horario_saida TIME NOT NULL DEFAULT '00:00',
    horario_chegada TIME NOT NULL DEFAULT '05:00',
    tempo_viagem INT NOT NULL DEFAULT 5,
    preco NUMERIC(10,2) NOT NULL DEFAULT 100.00
);

-- Tabela de poltronas (controle de ocupação por viagem/dia)
CREATE TABLE IF NOT EXISTS poltrona_ocupada (
    id SERIAL PRIMARY KEY,
    dia_semana VARCHAR(10) NOT NULL,
    poltrona INT NOT NULL CHECK (poltrona BETWEEN 1 AND 10),
    ocupado BOOLEAN NOT NULL DEFAULT FALSE
);
