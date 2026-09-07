import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from app.core.idioma import t

class Prontuario_View:
    def __init__(self, master):
        self.janela = ttk.Toplevel(master)
        self.janela.title(t("menu_prontuarios"))
        self.janela.geometry("350x300")

        ttk.Label(self.janela, text=t("cadastro_prontuario"), font=("Arial", 14, "bold")).pack(pady=10)

        ttk.Label(self.janela, text=t("paciente_campo")).pack(anchor=W, padx=20)
        self.campo_paciente = ttk.Entry(self.janela, width=30)
        self.campo_paciente.pack(padx=20, pady=5)

        ttk.Label(self.janela, text=t("observacoes")).pack(anchor=W, padx=20)
        self.campo_observacoes = ttk.Entry(self.janela, width=30)
        self.campo_observacoes.pack(padx=20, pady=5)

        ttk.Button(self.janela, text=t("botao_salvar"), command=self.salvar, bootstyle=SUCCESS).pack(pady=15)

    def salvar(self):
        paciente = self.campo_paciente.get()
        observacoes = self.campo_observacoes.get()
        print(f"[TODO: ligar ao controller] Salvar prontuário: {paciente}, {observacoes}")