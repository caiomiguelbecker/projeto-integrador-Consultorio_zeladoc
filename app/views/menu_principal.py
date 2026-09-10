import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from app.core.idioma import Idioma, trocar_idioma

from app.views.convenio_view import Convenio_View
from app.views.especialidade_view import Especialidade_View
from app.views.exame_view import Exame_View
from app.views.usuario_view import Usuario_View
from app.views.medico_view import Medico_View
from app.views.paciente_view import Paciente_View
from app.views.consulta_view import Consulta_View
from app.views.prontuario_view import Prontuario_View

from app.controller.convenio_controller import Convenio_Controller
from app.controller.especialidade_controller import Especialidade_Controller
from app.controller.exame_controller import Exame_Controller
from app.controller.usuario_controller import Usuario_Controller
from app.controller.medico_controller import Medico_Controller
from app.controller.paciente_controller import Paciente_Controller
from app.controller.consulta_controller import Consulta_Controller
from app.controller.protuario_controller import Prontuario_Controller


class Menu_Principal:

    def __init__(self, root, daos):
        self.root = root
        self.daos = daos
        self.configurar_janela()
        self.criar_componentes()

    def configurar_janela(self):
        self.root.title(Idioma.t("app_titulo"))
        self.root.geometry("420x520")
        self.root.resizable(False, False)

    def criar_componentes(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.lbl_titulo = ttk.Label(
            self.root,
            text=Idioma.t("app_titulo"),
            font=("Arial", 22, "bold")
        )
        self.lbl_titulo.pack(pady=(25, 15))

        self.frm_botoes = ttk.Frame(self.root)
        self.frm_botoes.pack(pady=10, fill=X, padx=40)

        botoes = [
            (Idioma.t("menu_pacientes"), PRIMARY, self.abrir_pacientes),
            (Idioma.t("menu_medicos"), PRIMARY, self.abrir_medicos),
            (Idioma.t("menu_consultas"), PRIMARY, self.abrir_consultas),
            (Idioma.t("menu_prontuarios"), PRIMARY, self.abrir_prontuarios),
            (Idioma.t("menu_convenios"), INFO, self.abrir_convenios),
            (Idioma.t("menu_especialidades"), INFO, self.abrir_especialidades),
            (Idioma.t("menu_exames"), INFO, self.abrir_exames),
            (Idioma.t("menu_usuarios"), INFO, self.abrir_usuarios),
        ]

        for texto, estilo, comando in botoes:
            btn = ttk.Button(self.frm_botoes, text=texto, bootstyle=estilo, width=30, command=comando)
            btn.pack(pady=5)

        self.btn_idioma = ttk.Button(
            self.root,
            text=Idioma.t("menu_idioma"),
            bootstyle=(SECONDARY, OUTLINE),
            width=30,
            command=self.alternar_idioma
        )
        self.btn_idioma.pack(pady=(15, 5))

        self.btn_sair = ttk.Button(
            self.root,
            text=Idioma.t("menu_sair"),
            bootstyle=DANGER,
            width=30,
            command=self.root.destroy
        )
        self.btn_sair.pack(pady=5)

    def alternar_idioma(self):
        trocar_idioma()
        self.criar_componentes()

    def abrir_convenios(self):
        janela = ttk.Toplevel(self.root)
        controller = Convenio_Controller(self.daos["convenio"], None)
        view = Convenio_View(janela, controller)
        controller.view = view
        view.iniciar()

    def abrir_especialidades(self):
        janela = ttk.Toplevel(self.root)
        controller = Especialidade_Controller(self.daos["especialidade"], None)
        view = Especialidade_View(janela, controller)
        controller.view = view
        view.iniciar()

    def abrir_exames(self):
        janela = ttk.Toplevel(self.root)
        controller = Exame_Controller(self.daos["exame"], None)
        view = Exame_View(janela, controller)
        controller.view = view
        view.iniciar()

    def abrir_usuarios(self):
        janela = ttk.Toplevel(self.root)
        controller = Usuario_Controller(self.daos["usuario"], None)
        view = Usuario_View(janela, controller)
        controller.view = view
        view.iniciar()

    def abrir_medicos(self):
        janela = ttk.Toplevel(self.root)
        controller = Medico_Controller(
            self.daos["medico"], self.daos["especialidade"], self.daos["usuario"], None
        )
        view = Medico_View(janela, controller)
        controller.view = view
        view.iniciar()

    def abrir_pacientes(self):
        janela = ttk.Toplevel(self.root)
        controller = Paciente_Controller(self.daos["paciente"], self.daos["convenio"], None)
        view = Paciente_View(janela, controller)
        controller.view = view
        view.iniciar()

    def abrir_consultas(self):
        janela = ttk.Toplevel(self.root)
        controller = Consulta_Controller(
            self.daos["consulta"], self.daos["paciente"], self.daos["medico"], None
        )
        view = Consulta_View(janela, controller)
        controller.view = view
        view.iniciar()

    def abrir_prontuarios(self):
        janela = ttk.Toplevel(self.root)
        controller = Prontuario_Controller(self.daos["prontuario"], self.daos["paciente"], None)
        view = Prontuario_View(janela, controller)
        controller.view = view
        view.iniciar()