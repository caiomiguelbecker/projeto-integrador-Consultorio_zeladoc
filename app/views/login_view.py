import os

import ttkbootstrap as ttk
from ttkbootstrap.constants import LEFT, PRIMARY, INFO
from tkinter import messagebox
from PIL import Image, ImageTk

from app.core import idioma

CAMINHO_LOGO = os.path.join(
    os.path.dirname(__file__), "..", "..", "assets", "logo.png"
)


class LoginView:

    IDIOMAS = {"Português": "pt", "English": "en"}

    def __init__(self, usuario_controller, ao_autenticar):
        self._ao_autenticar = ao_autenticar
        self._controller = usuario_controller

        self.janela = ttk.Window(themename="flatly")
        self.janela.resizable(False, False)

        self._montar_tela()
        self._atualizar_textos()
        self._centralizar()

    def _centralizar(self):
        self.janela.update_idletasks()
        largura, altura = 380, 460
        x = (self.janela.winfo_screenwidth() // 2) - (largura // 2)
        y = (self.janela.winfo_screenheight() // 2) - (altura // 2)
        self.janela.geometry(f"{largura}x{altura}+{x}+{y}")

    def _montar_tela(self):
        frame_topo = ttk.Frame(self.janela)
        frame_topo.pack(fill="x", padx=10, pady=(10, 0))

        self.idioma_var = ttk.StringVar()
        self.combo_idioma = ttk.Combobox(
            frame_topo,
            textvariable=self.idioma_var,
            values=list(self.IDIOMAS.keys()),
            state="readonly",
            width=10,
        )
        self.combo_idioma.pack(side="right")
        self.combo_idioma.bind("<<ComboboxSelected>>", self._trocar_idioma)

        frame = ttk.Frame(self.janela, padding=20)
        frame.pack(fill="both", expand=True)

        self._montar_logo(frame)

        self.lbl_email = ttk.Label(frame)
        self.lbl_email.pack(anchor="w")
        self.entry_email = ttk.Entry(frame, width=32)
        self.entry_email.pack(pady=(0, 10))

        self.lbl_senha = ttk.Label(frame)
        self.lbl_senha.pack(anchor="w")
        self.entry_senha = ttk.Entry(frame, width=32, show="*")
        self.entry_senha.pack(pady=(0, 20))
        self.entry_senha.bind("<Return>", lambda e: self._fazer_login())

        self.btn_entrar = ttk.Button(frame, command=self._fazer_login, bootstyle="danger", width=20)
        self.btn_entrar.pack(pady=(10, 0))

    def _montar_logo(self, parent):
        try:
            imagem = Image.open(CAMINHO_LOGO)
            imagem.thumbnail((150, 150))
            self.logo_img = ImageTk.PhotoImage(imagem)
            ttk.Label(parent, image=self.logo_img).pack(pady=(0, 20))
        except (FileNotFoundError, OSError):
            logo_frame = ttk.Frame(parent)
            logo_frame.pack(pady=(0, 20))
            ttk.Label(logo_frame, text="ZELA", font=("Segoe UI", 24, "bold"), bootstyle=PRIMARY).pack(side=LEFT)
            ttk.Label(logo_frame, text="DOC", font=("Segoe UI", 24, "bold"), bootstyle=INFO).pack(side=LEFT)

    def _trocar_idioma(self, event=None):
        codigo = self.IDIOMAS[self.idioma_var.get()]
        idioma.Idioma.definir(codigo)
        self._atualizar_textos()

    def _atualizar_textos(self):
        self.janela.title(idioma.t("Login"))
        self.lbl_email.config(text=idioma.t("Email"))
        self.lbl_senha.config(text=idioma.t("Senha"))
        self.btn_entrar.config(text=idioma.t("Entrar"))
        self.idioma_var.set("Português" if idioma.Idioma.ATUAL == "pt" else "English")

    def _fazer_login(self):
        email = self.entry_email.get().strip()
        senha = self.entry_senha.get().strip()

        if not email or not senha:
            messagebox.showwarning(idioma.t("Aviso"), idioma.t("Campos Obrigatórios!"))
            return

        usuario = self._controller.autenticar(email, senha)

        if usuario is None:
            messagebox.showerror(idioma.t("Erro"), idioma.t("Login ou Credenciais Inválidas!"))
            return

        self.janela.destroy()
        self._ao_autenticar(usuario)