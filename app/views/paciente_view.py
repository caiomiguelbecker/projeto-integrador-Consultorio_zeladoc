import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class Paciente_View:
    def __init__(self, master):
        self.janela = ttk.Toplevel(master)
        self.janela.title("Pacientes")
        self.janela.geometry("350x300")

        ttk.Label(self.janela, text="Cadastro de Paciente", font=("Arial", 14, "bold")).pack(pady=10)

        ttk.Label(self.janela, text="Nome:").pack(anchor=W, padx=20)
        self.campo_nome = ttk.Entry(self.janela, width=30)
        self.campo_nome.pack(padx=20, pady=5)

        ttk.Label(self.janela, text="Data de nascimento (AAAA-MM-DD):").pack(anchor=W, padx=20)
        self.campo_data = ttk.Entry(self.janela, width=30)
        self.campo_data.pack(padx=20, pady=5)

        ttk.Button(self.janela, text="Salvar", command=self.salvar, bootstyle=SUCCESS).pack(pady=15)

    def salvar(self):
        nome = self.campo_nome.get()
        data = self.campo_data.get()
        print(f"[TODO: ligar ao controller] Salvar paciente: {nome}, {data}")