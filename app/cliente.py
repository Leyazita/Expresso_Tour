from database import conectar

class Cliente:
    def __init__(self, cpf, nome, nascimento, senha):
        self.cpf = cpf
        self.nome = nome
        self.nascimento = nascimento
        self.senha = senha

    def salvar(self):
        conn = conectar()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO cliente (cpf, nome, nascimento, senha) VALUES (%s, %s, %s, %s)",
            (self.cpf, self.nome, self.nascimento, self.senha)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def autenticar(cpf, senha):
        conn = conectar()
        cur = conn.cursor()
        cur.execute("SELECT * FROM cliente WHERE cpf = %s AND senha = %s", (cpf, senha))
        user = cur.fetchone()
        conn.close()
        return user is not None

    @staticmethod
    def buscar_por_cpf(cpf):
        conn = conectar()
        cur = conn.cursor()
        cur.execute("SELECT cpf, nome, nascimento, senha FROM cliente WHERE cpf = %s", (cpf,))
        dados = cur.fetchone()
        conn.close()
        if dados:
            return Cliente(*dados)
        return None

    def alterar_senha(self, nova_senha):
        conn = conectar()
        cur = conn.cursor()
        cur.execute("UPDATE cliente SET senha = %s WHERE cpf = %s", (nova_senha, self.cpf))
        conn.commit()
        conn.close()
        
    def alterar_nome(self, novo_nome):
        conn = conectar()
        cur = conn.cursor()
        cur.execute(
            "UPDATE cliente SET nome = %s WHERE cpf = %s",
            (novo_nome, self.cpf)
        )
        conn.commit()
        conn.close()

    def alterar_cpf(self, novo_cpf):
        conn = conectar()
        cur = conn.cursor()
        cur.execute(
            "UPDATE cliente SET cpf = %s WHERE cpf = %s",
            (novo_cpf, self.cpf)
        )
        conn.commit()
        conn.close()
        self.cpf = novo_cpf  # Atualiza no objeto também


    def __str__(self):
        return f"Cliente(cpf={self.cpf}, nome={self.nome}, nascimento={self.nascimento})"
