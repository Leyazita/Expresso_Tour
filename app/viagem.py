from database import conectar

class Viagem:
    def __init__(self, dia_semana, horario_saida='00:00', horario_chegada='05:00', tempo_viagem=5, preco=100.0):
        self.dia_semana = dia_semana
        self.horario_saida = horario_saida
        self.horario_chegada = horario_chegada
        self.tempo_viagem = tempo_viagem
        self.preco = preco

    def salvar(self):
        conn = conectar()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO viagem (dia_semana, horario_saida, horario_chegada, tempo_viagem, preco) VALUES (%s, %s, %s, %s, %s)",
            (self.dia_semana, self.horario_saida, self.horario_chegada, self.tempo_viagem, self.preco)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def listar():
        conn = conectar()
        cur = conn.cursor()
        cur.execute("SELECT dia_semana, horario_saida, horario_chegada, tempo_viagem, preco FROM viagem")
        viagens = cur.fetchall()
        conn.close()
        return viagens


class Onibus:
    @staticmethod
    def listar_poltronas_ocupadas(dia_semana):
        conn = conectar()
        cur = conn.cursor()
        cur.execute("SELECT poltrona, ocupado FROM poltrona_ocupada WHERE dia_semana = %s", (dia_semana,))
        poltronas = cur.fetchall()
        conn.close()
        return poltronas

    @staticmethod
    def ocupar_poltrona(dia_semana, poltrona):
        conn = conectar()
        cur = conn.cursor()
        cur.execute(
            "UPDATE poltrona_ocupada SET ocupado = TRUE WHERE dia_semana = %s AND poltrona = %s",
            (dia_semana, poltrona)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def inicializar_poltronas():
        dias = ['Segunda', 'Quarta', 'Sexta']
        conn = conectar()
        cur = conn.cursor()
        for dia in dias:
            for i in range(1, 11):
                cur.execute("INSERT INTO poltrona_ocupada (dia_semana, poltrona, ocupado) VALUES (%s, %s, FALSE) ON CONFLICT DO NOTHING", (dia, i))
        conn.commit()
        conn.close()
        
    @staticmethod
    def liberar_poltrona(dia_semana, poltrona):
        conn = conectar()
        cur = conn.cursor()
        cur.execute(
            "UPDATE poltrona_ocupada SET ocupado = FALSE WHERE dia_semana = %s AND poltrona = %s",
            (dia_semana, poltrona)
        )
        conn.commit()
        conn.close()
