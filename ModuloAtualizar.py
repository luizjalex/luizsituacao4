from ConexaoBD import conectar
import mysql.connector
from tkinter import messagebox

def atualizarCadastro(data, nome, origem, destino, forma):
    conexao, cursor = conectar()
    try:
        sql = f"""UPDATE tb_pacotes-viagens
            SET data_viagem='{data}', nome_cliente'{nome}',
            local_origem='{origem}', local_destino='{destino}', forma_pagamento='{forma}' WHERE id_pro='{id}'
              """
        cursor.execute(sql)
        conexao.commit()
        messagebox.showinfo("Atualizar",
            "Cadastro atualizado!")
        return True
    except mysql.connector.Error as falha:
        messagebox.showerror("Falha",
            "Falha ao atualizar"+str(falha))
        return False
    finally:
        conexao.close()
        cursor.close()