import os

import ttkbootstrap as ttk
from ttkbootstrap.constants import PRIMARY, INFO, DANGER, LEFT, X, BOTH
from PIL import Image, ImageTk

# Caminho da logo: app/views/menu_principal.py -> volta 2 pastas -> assets/logo.png
CAMINHO_LOGO = os.path.join(
    os.path.dirname(__file__), "..", "..", "assets", "logo.png"
)


class Menu_Principal:
    """
    Tela de menu principal do ZelaDoc.
    Recebe a janela (root) já criada pelo Zeladoc_Application e o
    dicionário de DAOs, para poder repassá-los às próximas telas.
    """

    def __init__(self, master, daos):
        self.master = master
        self.daos = daos

        self.master.title("Menu Principal")
        self.master.geometry("1100x850")
        self.master.minsize(950, 700)

        self._montar_layout()

    # ------------------------------------------------------------------
    def _montar_layout(self):
        container = ttk.Frame(self.master, padding=40)
        container.pack(expand=True, fill=BOTH)

        container.columnconfigure(0, weight=1)
        container.columnconfigure(1, weight=2)
        container.columnconfigure(2, weight=1)

        self._montar_menu_esquerda(container)
        self._montar_centro(container)
        self._montar_menu_direita(container)

    # ------------------------------------------------------------------
    def _montar_menu_esquerda(self, parent):
        frame = ttk.Frame(parent)
        frame.grid(row=0, column=0, sticky="n", padx=10)

        itens = [
            ("👤  Pacientes", PRIMARY, self.abrir_pacientes),
            ("🩺  Médicos", PRIMARY, self.abrir_medicos),
            ("🔬  Consultas", PRIMARY, self.abrir_consultas),
            ("📋  Prontuários", PRIMARY, self.abrir_prontuarios),
            ("🛡  Convênios", INFO, self.abrir_convenios),
        ]

        for texto, estilo, comando in itens:
            btn = ttk.Button(
                frame, text=texto, bootstyle=estilo, width=22, command=comando
            )
            btn.pack(pady=6, fill=X, ipady=8)

    # ------------------------------------------------------------------
    def _montar_logo(self, parent):
        """Carrega a imagem da logo (assets/logo.png). Se não encontrar,
        cai para o texto 'ZELADOC' como alternativa, sem quebrar a tela."""
        try:
            imagem = Image.open(CAMINHO_LOGO)
            imagem.thumbnail((580, 580)) 
            self.logo_img = ImageTk.PhotoImage(imagem)  

            ttk.Label(parent, image=self.logo_img).pack(pady=(20, 10))
        except (FileNotFoundError, OSError):
            logo_frame = ttk.Frame(parent)
            logo_frame.pack(pady=(20, 10))
            ttk.Label(
                logo_frame,
                text="ZELA",
                font=("Segoe UI", 34, "bold"),
                bootstyle=PRIMARY,
            ).pack(side=LEFT)
            ttk.Label(
                logo_frame, text="DOC", font=("Segoe UI", 34, "bold"), bootstyle=INFO
            ).pack(side=LEFT)

    
    def _montar_centro(self, parent):
        frame = ttk.Frame(parent)
        frame.grid(row=0, column=1, sticky="n")

        self._montar_logo(frame)

        self.idioma_var = ttk.StringVar(value="English")
        idioma_combo = ttk.Combobox(
            frame,
            textvariable=self.idioma_var,
            values=["Português", "English"],
            state="readonly",
        )
        idioma_combo.pack(pady=(30, 12), fill=X, padx=20, ipady=4)

        sair_btn = ttk.Button(
            frame, text="↪  Sair", bootstyle=DANGER, width=22, command=self.sair
        )
        sair_btn.pack(pady=6, padx=20, fill=X, ipady=8)

   
    def _montar_menu_direita(self, parent):
        frame = ttk.Frame(parent)
        frame.grid(row=0, column=2, sticky="n", padx=10)

        itens = [
            ("⭐  Especialidades", INFO, self.abrir_especialidades),
            ("🧾  Exames", INFO, self.abrir_exames),
            ("👥  Usuários", INFO, self.abrir_usuarios),
        ]

        for texto, estilo, comando in itens:
            btn = ttk.Button(
                frame, text=texto, bootstyle=estilo, width=22, command=comando
            )
            btn.pack(pady=6, fill=X, ipady=8)

   
    def abrir_pacientes(self):
        from app.views.paciente_view import Paciente_View
        Paciente_View(self.janela)

       

    def abrir_medicos(self):
        print("Abrir tela: Médicos")
       

    def abrir_consultas(self):
        print("Abrir tela: Consultas")
       

    def abrir_prontuarios(self):
        print("Abrir tela: Prontuários")
        

    def abrir_convenios(self):
        print("Abrir tela: Convênios")
       

    def abrir_especialidades(self):
        print("Abrir tela: Especialidades")
       

    def abrir_exames(self):
        print("Abrir tela: Exames")
        

    def abrir_usuarios(self):
        print("Abrir tela: Usuários")
     

    def sair(self):
        self.master.destroy()