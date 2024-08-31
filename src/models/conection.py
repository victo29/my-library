import mysql.connector

def connection():
    # Conectar ao banco de dados MySQL
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="victor@123456",
        database="minha_biblioteca"
    )
    return conn