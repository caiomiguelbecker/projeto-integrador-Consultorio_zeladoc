import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from app.core.idioma import t, trocar_idioma

class Menu_Principal_View:

    def __init__(self):
        self.janela = ttk.Window(themename="flatly")
        self.janela.title("ZELADOC")
        self.janela.geometry("300x560")

        self.lbl_titulo = ttk.Label(self.janela, text="ZELADOC", font=("Arial", 18, "bold"))
        self.lbl_titulo.pack(pady=15)

        self.btn_pacientes = ttk.Button(self.janela, text=t("menu_pacientes"), command=self.abrir_pacientes, bootstyle=PRIMARY, width=20)
        self.btn_pacientes.pack(pady=6)

        self.btn_medicos = ttk.Button(self.janela, text=t("menu_medicos"), command=self.abrir_medicos, bootstyle=PRIMARY, width=20)
        self.btn_medicos.pack(pady=6)

        self.btn_consultas = ttk.Button(self.janela, text=t("menu_consultas"), command=self.abrir_consultas, bootstyle=PRIMARY, width=20)
        self.btn_consultas.pack(pady=6)

        self.btn_usuarios = ttk.Button(self.janela, text=t("menu_usuarios"), command=self.abrir_usuarios, bootstyle=PRIMARY, width=20)
        self.btn_usuarios.pack(pady=6)

        self.btn_convenios = ttk.Button(self.janela, text=t("menu_convenios"), command=self.abrir_convenios, bootstyle=PRIMARY, width=20)
        self.btn_convenios.pack(pady=6)

        self.btn_especialidades = ttk.Button(self.janela, text=t("menu_especialidades"), command=self.abrir_especialidades, bootstyle=PRIMARY, width=20)
        self.btn_especialidades.pack(pady=6)

        self.btn_exames = ttk.Button(self.janela, text=t("menu_exames"), command=self.abrir_exames, bootstyle=PRIMARY, width=20)
        self.btn_exames.pack(pady=6)

        self.btn_prontuarios = ttk.Button(self.janela, text=t("menu_prontuarios"), command=self.abrir_prontuarios, bootstyle=PRIMARY, width=20)
        self.btn_prontuarios.pack(pady=6)

        self.btn_idioma = ttk.Button(self.janela, text=t("menu_idioma"), command=self.mudar_idioma, bootstyle=SECONDARY, width=20)
        self.btn_idioma.pack(pady=6)

        self.btn_sair = ttk.Button(self.janela, text=t("menu_sair"), command=self.janela.destroy, bootstyle=DANGER, width=20)
        self.btn_sair.pack(pady=6)

    def mudar_idioma(self):
        trocar_idioma()
        self.btn_pacientes.config(text=t("menu_pacientes"))
        self.btn_medicos.config(text=t("menu_medicos"))
        self.btn_consultas.config(text=t("menu_consultas"))
        self.btn_usuarios.config(text=t("menu_usuarios"))
        self.btn_convenios.config(text=t("menu_convenios"))
        self.btn_especialidades.config(text=t("menu_especialidades"))
        self.btn_exames.config(text=t("menu_exames"))
        self.btn_prontuarios.config(text=t("menu_prontuarios"))
        self.btn_idioma.config(text=t("menu_idioma"))
        self.btn_sair.config(text=t("menu_sair"))

    def abrir_pacientes(self):
        from app.views.paciente_view import Paciente_View
        Paciente_View(self.janela)

    def abrir_medicos(self):
        from app.views.medico_view import Medico_View
        Medico_View(self.janela)

    def abrir_consultas(self):
        from app.views.consulta_view import Consulta_View
        Consulta_View(self.janela)

    def abrir_usuarios(self):
        from app.views.usuario_view import Usuario_View
        Usuario_View(self.janela)

    def abrir_convenios(self):
        from app.views.convenio_view import Convenio_View
        Convenio_View(self.janela)

    def abrir_especialidades(self):
        from app.views.especialidade_view import Especialidade_View
        Especialidade_View(self.janela)

    def abrir_exames(self):
        from app.views.exame_view import Exame_View
        Exame_View(self.janela)

    def abrir_prontuarios(self):
        from app.views.prontuario_view import Prontuario_View
        Prontuario_View(self.janela)

    def iniciar(self):
        self.janela.mainloop()