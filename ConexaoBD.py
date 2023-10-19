import mysql.connector
from tkinter import messagebox

def conectar():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="bd_situacao_02"
        )
        cursor = conexao.cursor()
        print("Conectado com sucesso ao banco")
        return conexao, cursor
    except mysql.connector.Error as falha:
        messagebox.showerror("Erro", "Falha na conexão com BD"+ str(falha))
        return None, None

