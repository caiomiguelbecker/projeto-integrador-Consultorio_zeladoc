import os

import pywinstyles
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import LEFT, X, BOTH
from app.core.tooltip_utils import Tooltip
from PIL import Image, ImageTk

from app.core.idioma import Idioma, t
from app.core.icone_utils import aplicar_icone
from app.core.janela_utils import maximizar_respeitando_taskbar, bloquear_minimizar

CAMINHO_LOGO = os.path.join(
    os.path.dirname(__file__), "..", "..", "assets", "logo.png"
)


class Menu_Principal:

    def __init__(self, master, daos):
        self.master = master
        self.daos = daos
        self.modo_escuro = False

        self._janela_pacientes = None
        self._janela_medicos = None
        self._janela_consultas = None
        self._janela_prontuarios = None
        self._janela_convenios = None
        self._janela_especialidades = None
        self._janela_exames = None
        self._janela_usuarios = None

        aplicar_icone(self.master)
        self.master.resizable(False, False)
        maximizar_respeitando_taskbar(self.master)
        bloquear_minimizar(self.master)

        self._montar_layout()

    def _configurar_estilos_menu(self):
        estilo = ttk.Style()
        cores = estilo.colors
        fonte = ("Segoe UI", 12)

        mapa_cores = {
            "MenuPrimary": cores.primary,
            "MenuInfo": cores.info,
            "MenuDanger": cores.danger,
        }

        for nome, cor in mapa_cores.items():
            estilo.configure(
                f"{nome}.TButton",
                font=fonte,
                background=cor,
                foreground=cores.selectfg,
                borderwidth=0,
            )
            estilo.map(f"{nome}.TButton", background=[("active", cor)])

            estilo.configure(
                f"{nome}Outline.TButton",
                font=fonte,
                background=cores.bg,
                foreground=cor,
                bordercolor=cor,
                borderwidth=2,
            )
            estilo.map(f"{nome}Outline.TButton", background=[("active", cores.bg)])

    def _aplicar_hover(self, botao, nome_base):
        def ao_entrar(event):
            botao.configure(style=f"{nome_base}Outline.TButton")

        def ao_sair(event):
            botao.configure(style=f"{nome_base}.TButton")

        botao.bind("<Enter>", ao_entrar)
        botao.bind("<Leave>", ao_sair)

    def _montar_layout(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        self._configurar_estilos_menu()

        self.master.title("ZelaDoc - Menu Principal")

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
            (f"  {t('menu_pacientes')}", self.abrir_pacientes,
             "Cadastrar, editar e consultar pacientes"),
            (f"  {t('menu_medicos')}", self.abrir_medicos,
             "Gerenciar médicos e suas especialidades"),
            (f"  {t('menu_consultas')}", self.abrir_consultas,
             "Agendar e acompanhar consultas"),
            (f"  {t('menu_prontuarios')}", self.abrir_prontuarios,
             "Consultar o histórico clínico dos pacientes"),
        ]

        for texto, comando, dica in itens:
            btn = ttk.Button(
                frame, text=texto, style="MenuPrimary.TButton", width=40, command=comando
            )
            btn.pack(pady=6, fill=X, ipady=20)
            self._aplicar_hover(btn, "MenuPrimary")
            Tooltip(btn, dica)

    def _montar_logo(self, parent):
        try:
            imagem = Image.open(CAMINHO_LOGO).convert("RGBA")
            dados = imagem.getdata()
            nova_imagem = []
            for r, g, b, a in dados:
                if r > 240 and g > 240 and b > 240:
                    nova_imagem.append((r, g, b, 0))
                else:
                    nova_imagem.append((r, g, b, a))
            imagem.putdata(nova_imagem)
            imagem.thumbnail((580, 580))
            self.logo_img = ImageTk.PhotoImage(imagem)
            ttk.Label(parent, image=self.logo_img).pack(pady=(20, 10))
        except (FileNotFoundError, OSError):
            logo_frame = ttk.Frame(parent)
            logo_frame.pack(pady=(20, 10))
            ttk.Label(
                logo_frame, text="ZELA", font=("Segoe UI", 30, "bold"), bootstyle="primary"
            ).pack(side=LEFT)
            ttk.Label(
                logo_frame, text="DOC", font=("Segoe UI", 30, "bold"), bootstyle="info"
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

        texto_tema = "☀️  Modo Claro" if self.modo_escuro else "🌙  Modo Escuro"
        btn_tema = ttk.Button(
            frame, text=texto_tema, bootstyle="secondary-outline", width=22,
            command=self._alternar_tema
        )
        btn_tema.pack(pady=(0, 12), padx=20, fill=X, ipady=6)
        Tooltip(btn_tema, t('dica_alternar_tema'))  

        sair_btn = ttk.Button(
            frame, text=f"↪  {t('menu_sair')}", style="MenuDanger.TButton", width=22, command=self.sair
        )
        sair_btn.pack(pady=6, padx=20, fill=X, ipady=10)
        self._aplicar_hover(sair_btn, "MenuDanger")
        Tooltip(sair_btn, t('dica_sair'))

    def _alternar_tema(self):
        self.modo_escuro = not self.modo_escuro
        novo_tema = "darkly" if self.modo_escuro else "flatly"
        ttk.Style().theme_use(novo_tema)
        self._montar_layout()

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
            (f"  {t('menu_especialidades')}", self.abrir_especialidades,
             "Cadastrar especialidades médicas"),
            (f"  {t('menu_exames')}", self.abrir_exames,
             "Cadastrar tipos de exames"),
            (f"  {t('menu_usuarios')}", self.abrir_usuarios,
             "Gerenciar usuários com acesso ao sistema"),
            (f"  {t('menu_convenios')}", self.abrir_convenios,
             "Cadastrar convênios aceitos"),
        ]

        for texto, comando, dica in itens:
            btn = ttk.Button(
                frame, text=texto, style="MenuInfo.TButton", width=40, command=comando
            )
            btn.pack(pady=6, fill=X, ipady=20)
            self._aplicar_hover(btn, "MenuInfo")
            Tooltip(btn, dica)

    

    def _abrir_janela(self, atributo_janela, classe_view, classe_controller, **kwargs_controller):
        janela_existente = getattr(self, atributo_janela)

        if janela_existente is not None and janela_existente.winfo_exists():
            janela_existente.lift()
            janela_existente.focus_force()
            return

        janela = tk.Toplevel(self.master)
        pywinstyles.apply_style(janela, "dark")  # <-- adiciona aqui
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