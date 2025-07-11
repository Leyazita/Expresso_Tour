import psycopg2

def conectar():
    return psycopg2.connect(
        dbname="expresso_tour",
        user="expresso",
        password="senha123",
        host="localhost",
        port="5432"
    )
