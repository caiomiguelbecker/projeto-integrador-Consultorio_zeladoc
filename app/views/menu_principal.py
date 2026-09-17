import os

import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import PRIMARY, INFO, DANGER, LEFT, X, BOTH
from PIL import Image, ImageTk

from app.core.idioma import Idioma, t
from app.core.icone_utils import aplicar_icone

CAMINHO_LOGO = os.path.join(
    os.path.dirname(__file__), "..", "..", "assets", "logo.png"
)


class Menu_Principal:

    def __init__(self, master, daos):
        self.master = master
        self.daos = daos

        self._janela_pacientes = None
        self._janela_medicos = None
        self._janela_consultas = None
        self._janela_prontuarios = None
        self._janela_convenios = None
        self._janela_especialidades = None
        self._janela_exames = None
        self._janela_usuarios = None

        aplicar_icone(self.master)
        self.master.state("zoomed")
        self.master.resizable(False, False)

        self._montar_layout()
   
    def _configurar_estilos_menu(self):
        estilo = ttk.Style()
        cores = estilo.colors

        mapa_cores = {
            "MenuPrimary.TButton": cores.primary,
            "MenuInfo.TButton": cores.info,
            "MenuDanger.TButton": cores.danger,
        }

        for nome_estilo, cor in mapa_cores.items():
            estilo.configure(
                nome_estilo,
                font=("Arial", 12),
                background=cor,
                foreground=cores.selectfg,
                borderwidth=0,
                focuscolor=cor,
            )
            estilo.map(nome_estilo, background=[("active", cor)])
   
   
    def _montar_layout(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        self._configurar_estilos_menu()
            
        self.master.title(t("app_titulo") + " - " + t("menu_sair") if False else "ZelaDoc - Menu Principal")

        container = ttk.Frame(self.master, padding=40)
        container.pack(expand=True, fill=BOTH)

        container.columnconfigure(0, weight=1)
        container.columnconfigure(1, weight=2)
        container.columnconfigure(2, weight=1)

        container.rowconfigure(0, weight=1)  
        container.rowconfigure(2, weight=0)  
        container.rowconfigure(3, weight=1) 

        self._montar_menu_esquerda(container)
        self._montar_centro(container)
        self._montar_menu_direita(container)

    
    def _montar_menu_esquerda(self, parent):
        frame = ttk.Frame(parent)
        frame.grid(row=2, column=0, sticky="ns", padx=10)

        itens = [
            (f"  {t('menu_pacientes')}", "MenuPrimary.TButton", self.abrir_pacientes),
            (f"  {t('menu_medicos')}", "MenuPrimary.TButton", self.abrir_medicos),
            (f"  {t('menu_consultas')}", "MenuPrimary.TButton", self.abrir_consultas),
            (f"  {t('menu_prontuarios')}", "MenuPrimary.TButton", self.abrir_prontuarios),
        ]

        for texto, nome_estilo, comando in itens:
            btn = ttk.Button(
                frame, text=texto, style=nome_estilo, width=40, command=comando
            )
            btn.pack(pady=6, fill=X, ipady=20)
    
    def _montar_logo(self, parent):
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
                font=("Segoe UI", 30, "bold"),
                bootstyle=PRIMARY,
            ).pack(side=LEFT)
            ttk.Label(
                logo_frame, text="DOC", font=("Segoe UI", 30, "bold"), bootstyle=INFO
            ).pack(side=LEFT)

   
    def _montar_centro(self, parent):
        frame = ttk.Frame(parent)
        frame.grid(row=2, column=1, sticky="n")

        self._montar_logo(frame)

        rotulo_atual = "Português" if Idioma.ATUAL == "pt" else "English"
        self.idioma_var = ttk.StringVar(value=rotulo_atual)
        idioma_combo = ttk.Combobox(
            frame,
            textvariable=self.idioma_var,
            values=["Português", "English"],
            state="readonly",
        )
        idioma_combo.pack(pady=(30, 12), fill=X, padx=20, ipady=4)
        
        idioma_combo.bind("<<ComboboxSelected>>", self._ao_trocar_idioma)

        sair_btn = ttk.Button(
            frame, text=f"↪  {t('menu_sair')}", style="MenuDanger.TButton", width=22, command=self.sair
        )
        sair_btn.pack(pady=6, padx=20, fill=X, ipady=10)

   
    def _ao_trocar_idioma(self, event=None):
        novo_codigo = "pt" if self.idioma_var.get() == "Português" else "en"

        if novo_codigo == Idioma.ATUAL:
            return  

        Idioma.definir(novo_codigo)
        self._montar_layout() 

   
    def _montar_menu_direita(self, parent):
        frame = ttk.Frame(parent)
        frame.grid(row=2, column=2, sticky="ns", padx=10) 

        itens = [
            (f"  {t('menu_especialidades')}", "MenuInfo.TButton", self.abrir_especialidades),
            (f"  {t('menu_exames')}", "MenuInfo.TButton", self.abrir_exames),
            (f"  {t('menu_usuarios')}", "MenuInfo.TButton", self.abrir_usuarios),
            (f"  {t('menu_convenios')}", "MenuInfo.TButton", self.abrir_convenios),
        ]

        for texto, nome_estilo, comando in itens:
            btn = ttk.Button(
                frame, text=texto, style=nome_estilo, width=40, command=comando
            )
            btn.pack(pady=6, fill=X, ipady=20)
    
    def _abrir_janela(self, atributo_janela, classe_view, classe_controller, **kwargs_controller):
        janela_existente = getattr(self, atributo_janela)

        if janela_existente is not None and janela_existente.winfo_exists():
            janela_existente.lift()
            janela_existente.focus_force()
            return

        janela = tk.Toplevel(self.master, background="#FFFFFF")
        setattr(self, atributo_janela, janela)

        controller = classe_controller(view=None, **kwargs_controller)
        controller.view = classe_view(janela, controller)
        controller.view.iniciar()

    
    def abrir_pacientes(self):
        from app.views.paciente_view import Paciente_View
        from app.controller.paciente_controller import Paciente_Controller

        self._abrir_janela(
            "_janela_pacientes",
            Paciente_View,
            Paciente_Controller,
            dao=self.daos["paciente"],
            convenio_dao=self.daos["convenio"],
        )

    def abrir_medicos(self):
        from app.views.medico_view import Medico_View
        from app.controller.medico_controller import Medico_Controller

        self._abrir_janela(
            "_janela_medicos",
            Medico_View,
            Medico_Controller,
            dao=self.daos["medico"],
            especialidade_dao=self.daos["especialidade"],
            usuario_dao=self.daos["usuario"],
        )

    def abrir_consultas(self):
        from app.views.consulta_view import Consulta_View
        from app.controller.consulta_controller import Consulta_Controller

        self._abrir_janela(
            "_janela_consultas",
            Consulta_View,
            Consulta_Controller,
            dao=self.daos["consulta"],
            paciente_dao=self.daos["paciente"],
            medico_dao=self.daos["medico"],
            exame_dao=self.daos["exame"],
            consulta_exame_dao=self.daos["consulta_exame"],
        )

    def abrir_prontuarios(self):
        from app.views.prontuario_view import Prontuario_View
        from app.controller.protuario_controller import Prontuario_Controller

        self._abrir_janela(
            "_janela_prontuarios",
            Prontuario_View,
            Prontuario_Controller,
            dao=self.daos["prontuario"],
            paciente_dao=self.daos["paciente"],
        )

    def abrir_convenios(self):
        from app.views.convenio_view import Convenio_View
        from app.controller.convenio_controller import Convenio_Controller

        self._abrir_janela(
            "_janela_convenios",
            Convenio_View,
            Convenio_Controller,
            dao=self.daos["convenio"],
        )

    def abrir_especialidades(self):
        from app.views.especialidade_view import Especialidade_View
        from app.controller.especialidade_controller import Especialidade_Controller

        self._abrir_janela(
            "_janela_especialidades",
            Especialidade_View,
            Especialidade_Controller,
            dao=self.daos["especialidade"],
        )

    def abrir_exames(self):
        from app.views.exame_view import Exame_View
        from app.controller.exame_controller import Exame_Controller

        self._abrir_janela(
            "_janela_exames",
            Exame_View,
            Exame_Controller,
            dao=self.daos["exame"],
        )

    def abrir_usuarios(self):
        from app.views.usuario_view import Usuario_View
        from app.controller.usuario_controller import Usuario_Controller

        self._abrir_janela(
            "_janela_usuarios",
            Usuario_View,
            Usuario_Controller,
            dao=self.daos["usuario"],
        )

    def sair(self):
        self.master.destroy()