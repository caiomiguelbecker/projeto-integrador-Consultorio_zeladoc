import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from app.core.idioma import t

class Especialidade_View:
    def __init__(self, master):
        self.janela = ttk.Toplevel(master)
        self.janela.title(t("menu_especialidades"))
        self.janela.geometry("350x220")

        ttk.Label(self.janela, text=t("cadastro_especialidade"), font=("Arial", 14, "bold")).pack(pady=10)

        ttk.Label(self.janela, text=t("nome")).pack(anchor=W, padx=20)
        self.campo_nome = ttk.Entry(self.janela, width=30)
        self.campo_nome.pack(padx=20, pady=5)

        ttk.Button(self.janela, text=t("botao_salvar"), command=self.salvar, bootstyle=SUCCESS).pack(pady=15)

    def salvar(self):
        nome = self.campo_nome.get()
        print(f"[TODO: ligar ao controller] Salvar especialidade: {nome}")