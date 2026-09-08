import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from app.core.idioma import t

class Medico_View:
    def __init__(self, master):
        self.janela = ttk.Toplevel(master)
        self.janela.title(t("menu_medicos"))
        self.janela.geometry("350x420")

        ttk.Label(self.janela, text=t("cadastro_medico"), font=("Arial", 14, "bold")).pack(pady=10)

        ttk.Label(self.janela, text=t("nome")).pack(anchor=W, padx=20)
        self.campo_nome = ttk.Entry(self.janela, width=30)
        self.campo_nome.pack(padx=20, pady=5)

        ttk.Label(self.janela, text=t("crm")).pack(anchor=W, padx=20)
        self.campo_crm = ttk.Entry(self.janela, width=30)
        self.campo_crm.pack(padx=20, pady=5)

        ttk.Label(self.janela, text=t("especialidade_campo")).pack(anchor=W, padx=20)
        self.campo_especialidade = ttk.Entry(self.janela, width=30)
        self.campo_especialidade.pack(padx=20, pady=5)

        ttk.Label(self.janela, text=t("usuario_login")).pack(anchor=W, padx=20)
        self.campo_usuario = ttk.Entry(self.janela, width=30)
        self.campo_usuario.pack(padx=20, pady=5)

        ttk.Button(self.janela, text=t("botao_salvar"), command=self.salvar, bootstyle=SUCCESS).pack(pady=15)

    def salvar(self):
        nome = self.campo_nome.get()
        crm = self.campo_crm.get()
        especialidade = self.campo_especialidade.get()
        usuario = self.campo_usuario.get()
        print(f"[TODO: ligar ao controller] Salvar médico: {nome}, {crm}, {especialidade}, {usuario}")