import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from app.core.idioma import t

class Usuario_View:
    def __init__(self, master):
        self.janela = ttk.Toplevel(master)
        self.janela.title(t("menu_usuarios"))
        self.janela.geometry("350x350")

        ttk.Label(self.janela, text=t("cadastro_usuario"), font=("Arial", 14, "bold")).pack(pady=10)

        ttk.Label(self.janela, text=t("nome")).pack(anchor=W, padx=20)
        self.campo_nome = ttk.Entry(self.janela, width=30)
        self.campo_nome.pack(padx=20, pady=5)

        ttk.Label(self.janela, text=t("email")).pack(anchor=W, padx=20)
        self.campo_email = ttk.Entry(self.janela, width=30)
        self.campo_email.pack(padx=20, pady=5)

        ttk.Label(self.janela, text=t("senha")).pack(anchor=W, padx=20)
        self.campo_senha = ttk.Entry(self.janela, width=30, show="*")
        self.campo_senha.pack(padx=20, pady=5)

        ttk.Button(self.janela, text=t("botao_salvar"), command=self.salvar, bootstyle=SUCCESS).pack(pady=15)

    def salvar(self):
        nome = self.campo_nome.get()
        email = self.campo_email.get()
        senha = self.campo_senha.get()
        print(f"[TODO: ligar ao controller] Salvar usuário: {nome}, {email}, {senha}")