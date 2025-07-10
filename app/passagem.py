from database import conectar

class Passagem:
    def __init__(self, cpf_cliente, data_ida, hora_ida, origem, destino, valor, pagamento, poltrona):
        self.cpf_cliente = cpf_cliente
        self.data_ida = data_ida
        self.hora_ida = hora_ida
        self.origem = origem
        self.destino = destino
        self.valor = valor
        self.pagamento = pagamento
        self.poltrona = poltrona

    def salvar(self):
        conn = conectar()
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO passagem (cpf_cliente, data_ida, hora_ida, origem, destino, valor, pagamento, poltrona)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING id
            """,
            (self.cpf_cliente, self.data_ida, self.hora_ida, self.origem,
             self.destino, self.valor, self.pagamento, self.poltrona)
        )
        self.id_passagem = cur.fetchone()[0]
        conn.commit()
        conn.close()

    def exibe_passagem(self, nome):
        print('|', '-' * 38, '|')
        print(f'|{f"CARTÃO DE EMBARQUE":^40}|')
        print('|', '-' * 38, '|')
        print(f'| ID da passagem: {self.id_passagem}')
        print(f'| Nome do passageiro: {nome}')
        print(f'| Documento CPF: {self.cpf_cliente}')
        print(f'| Poltrona: {self.poltrona}')
        print(f'| Valor: R${self.valor:.2f}')
        print(f'| Tipo de pagamento: {self.pagamento}')
        print(f'| Origem: {self.origem}')
        print(f'| Destino: {self.destino}')
        print(f'| Data: {self.data_ida}-feira')
        print(f'| Hora de partida: {self.hora_ida}')
        print('|', '-' * 38, '|')

    @staticmethod
    def buscar_por_cpf(cpf):
        conn = conectar()
        cur = conn.cursor()
        cur.execute("SELECT * FROM passagem WHERE cpf_cliente = %s", (cpf,))
        passagens = cur.fetchall()
        conn.close()
        return passagens

    @staticmethod
    def cancelar(cpf, id_passagem):
        conn = conectar()
        cur = conn.cursor()
        cur.execute("DELETE FROM passagem WHERE id = %s AND cpf_cliente = %s", (id_passagem, cpf))
        conn.commit()
        conn.close()
