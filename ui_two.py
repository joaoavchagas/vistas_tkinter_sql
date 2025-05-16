import tkinter as tk
import mysql.connector
from tkinter import messagebox
from datetime import date


def data_de_hoje():
    return date.today().strftime('%Y/%m/%d')

def salvar_visita():
    nome = entry_nome.get()
    documento = entry_documento.get()
    data = entry_data.get()
    motivo = entry_motivo.get()
    
    if nome and documento and data and motivo:
        try:
            conexao = mysql.connector.connect(
                host = "localhost",
                user ="root ",
                password = "",
                port = 3306,
                database ="cadastro"
            )
            cursor = conexao.cursor()
 
            sql ="insert into visitas (nome,documento,diadata,motivo)values (%s,%s,%s,%s)"
            valores = (nome,documento,data,motivo)
            cursor.execute(sql, valores)
            conexao.commit()
 
            label_status.config(text=f'Dados de "{nome}" salvos com sucesso!',fg="green")
            entry_nome.delete(0,tk.END)
            entry_documento.delete(0,tk.END)
            entry_data.delete(0,tk.END)
            entry_data.insert(0, data_de_hoje())
            entry_motivo.delete(0,tk.END)

            cursor.close()
            conexao.close()
        except mysql.connector.Error as erro:
            messagebox.showerror("Erro de conexão", f"Erro ao conectar ao banco:\n{erro}")
   
    else:
        label_status.config(text="Por favor, digite um nome.", fg="red")
        label_status.config(text="Por favor, digite um documento.", fg="red")
        label_status.config(text="Erro ao capturar data.", fg="red")
        label_status.config(text="Por favor, digite um motivo.", fg="red")

 
      
 
root = tk.Tk()
root.title("Salvar")
 
largura_janela = 450
altura_janela =400
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()
pos_x = (largura_tela // 2) - (largura_janela // 2)
por_y = (altura_tela //2 ) - (altura_janela //2)
root.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{por_y}")
 
label_nome = tk.Label(root, text="Digite seu nome")
label_nome.pack(pady=10)
entry_nome = tk.Entry(root, width=40)
entry_nome.pack(pady=5)

label_documento = tk.Label(root, text="Digite um de seus Documentos(RG ou CPF)")
label_documento.pack(pady=10)
entry_documento = tk.Entry(root, width=40)
entry_documento.pack(pady=5)

label_data = tk.Label(root, text="Data de hoje")
label_data.pack(pady=10)
entry_data = tk.Entry(root, width=40)
entry_data.insert(0, data_de_hoje())
entry_data.pack(pady=5)

label_motivo = tk.Label(root, text="Digite o motivo de sua visita")
label_motivo.pack(pady=10)
entry_motivo = tk.Entry(root, width=40)
entry_motivo.pack(pady=5)
 
botao_salvar = tk.Button(root,text="Salvar", command=salvar_visita)
botao_salvar.pack(pady=15)
 
label_status= tk.Label(root,text = "")
label_status.pack(pady=5)
 
root.mainloop()
 