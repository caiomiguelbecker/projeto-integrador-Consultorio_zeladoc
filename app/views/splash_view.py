import os

import ttkbootstrap as ttk
from PIL import Image, ImageTk

from app.core.icone_utils import aplicar_icone

CAMINHO_LOGO = os.path.join(
    os.path.dirname(__file__), "..", "..", "assets", "logo.png"
)


class Splash_View:

    def __init__(self, master, largura=420, altura=320):
        self.master = master

        self.master.overrideredirect(True)
        aplicar_icone(self.master)
        self._centralizar(largura, altura)

        frame = ttk.Frame(self.master, padding=30, bootstyle="white")
        frame.pack(fill="both", expand=True)

        self._montar_logo(frame)

        self.lbl_status = ttk.Label(
            frame,
            text="Iniciando...",
            font=("Segoe UI", 11, "bold"),
            foreground="#1F80AA",
        )
        self.lbl_status.pack(pady=(0, 12))

        self.barra = ttk.Progressbar(
            frame, mode="indeterminate",
            bootstyle="info-striped", length=280
        )
        self.barra.pack()
        self.barra.start(12)  

    def _montar_logo(self, parent):
        try:
            imagem = Image.open(CAMINHO_LOGO)
            imagem.thumbnail((220, 220))
            self.logo_img = ImageTk.PhotoImage(imagem)
            ttk.Label(parent, image=self.logo_img).pack(pady=(10, 20))
        except (FileNotFoundError, OSError):
            ttk.Label(
                parent, text="ZelaDoc", font=("Segoe UI", 26, "bold")
            ).pack(pady=(10, 20))

    def _centralizar(self, largura, altura):
        self.master.update_idletasks()
        x = (self.master.winfo_screenwidth() // 2) - (largura // 2)
        y = (self.master.winfo_screenheight() // 2) - (altura // 2)
        self.master.geometry(f"{largura}x{altura}+{x}+{y}")

    def atualizar(self, texto=None):
        if texto is not None:
            self.lbl_status.config(text=texto)
        self.master.update_idletasks()

    def encerrar(self):
        self.barra.stop()
        self.master.destroy()