from conn import db
import tkinter as tk
from tkinter import messagebox

def adicionar_aluno_ao_firebase(nome, matricula):
    if db:
        try:
            db.collection('alunos').document(matricula).set({'nome': nome, 'matricula': matricula})
            messagebox.showinfo("Sucesso", f"Aluno {nome} cadastrado.")
            
            entry_nome.delete(0, tk.END)
            entry_matricula.delete(0, tk.END)

        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao cadastrar: {e}")
    else:
        messagebox.showerror("Erro", "Banco de dados não conectado.")

root = tk.Tk()
root.title("Cadastro de Aluno no Sistema Escolar")

tk.Label(root, text="Nome do Aluno:").grid(row=0, column=0, padx=5, pady=5, sticky='w')
entry_nome = tk.Entry(root, width=40)
entry_nome.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Matrícula:").grid(row=1, column=0, padx=5, pady=5, sticky='w')
entry_matricula = tk.Entry(root, width=40)
entry_matricula.grid(row=1, column=1, padx=5, pady=5)

tk.Button(root, text="CADASTRAR ALUNO", 
          command=lambda: adicionar_aluno_ao_firebase(entry_nome.get(), entry_matricula.get())
          ).grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()