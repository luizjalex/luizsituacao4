from ConexaoBD import conectar
import mysql.connector
from tkinter import messagebox

def inserir(data, nome, origem, destino, forma):
    conexao, cursor = conectar()
    try:
        sql = f"""INSERT INTO tb_producao
                (data_viagem, nome_cliente, local_origem, local_destino, forma_pagamento)
                VALUES
                ('{data}','{nome}','{origem}','{destino}','{forma}')
                """
        cursor.execute(sql)
        conexao.commit()
        messagebox.showinfo("Cadastrado","Cadastrado com sucesso!")
        return True
    except mysql.connector.Error as falha:
        messagebox.showerror("Falha", "Falha ao cadastrar: "+str(falha))
        return False
    finally:
        conexao.close()
        cursor.close()