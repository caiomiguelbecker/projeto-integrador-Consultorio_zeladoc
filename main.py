import sys
import threading

import ttkbootstrap as ttk

from app.core.database import Database
from app.core.icone_utils import aplicar_icone

if sys.platform.startswith("win"):
    import ctypes

    try:
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            "zeladoc.consultorio.app.1"
        )
    except Exception:
        pass

from app.dao.convenio_dao import Convenio_DAO
from app.dao.especialidade_dao import Especialidade_DAO
from app.dao.exame_dao import Exame_DAO
from app.dao.usuario_dao import Usuario_DAO
from app.dao.medico_dao import Medico_DAO
from app.dao.paciente_dao import Paciente_DAO
from app.dao.consulta_dao import Consulta_DAO
from app.dao.consulta_exame_dao import Consulta_Exame_DAO
from app.dao.prontuario_dao import Prontuario_DAO
from app.controller.usuario_controller import Usuario_Controller
from app.views.menu_principal import Menu_Principal
from app.views.login_view import LoginView
from app.views.splash_view import Splash_View


class Zeladoc_Application:

    def __init__(self, progresso=None):
        self.database = Database()
        self.daos = self._criar_daos(progresso=progresso)
        self.usuario_controller = Usuario_Controller(self.daos["usuario"])

    def _criar_daos(self, progresso=None):
        def avancar(texto):
            if progresso:
                progresso(texto)

        avancar("Conectando ao banco de dados...")
        convenio_dao = Convenio_DAO(self.database)  

        avancar("Carregando convênios...")
        especialidade_dao = Especialidade_DAO(self.database)

        avancar("Carregando especialidades...")
        exame_dao = Exame_DAO(self.database)

        avancar("Carregando exames...")
        usuario_dao = Usuario_DAO(self.database)

        avancar("Carregando usuários...")
        medico_dao = Medico_DAO(self.database, especialidade_dao, usuario_dao)

        avancar("Carregando médicos...")
        paciente_dao = Paciente_DAO(self.database, convenio_dao)

        avancar("Carregando pacientes...")
        consulta_dao = Consulta_DAO(self.database, paciente_dao, medico_dao)

        avancar("Carregando consultas...")
        consulta_exame_dao = Consulta_Exame_DAO(self.database)
        prontuario_dao = Prontuario_DAO(self.database, paciente_dao)

        avancar("Bem vindo ao ZelaDoc... aguarde o carregamento!")
        

        return {
            "convenio": convenio_dao,
            "especialidade": especialidade_dao,
            "exame": exame_dao,
            "usuario": usuario_dao,
            "medico": medico_dao,
            "paciente": paciente_dao,
            "consulta": consulta_dao,
            "consulta_exame": consulta_exame_dao,
            "prontuario": prontuario_dao,
        }

    def iniciar(self):
        login = LoginView(self.usuario_controller, ao_autenticar=self._abrir_menu_principal)
        login.janela.mainloop()

    def _abrir_menu_principal(self, usuario):
        root = ttk.Window(themename="flatly")
        Menu_Principal(root, self.daos)
        root.mainloop()


def iniciar_com_splash():
    splash_root = ttk.Window(themename="flatly")
    splash = Splash_View(splash_root)

    estado = {}
    pending_after_ids = []

    def progresso(texto):
        after_id = splash_root.after(0, lambda: splash.atualizar(texto))
        pending_after_ids.append(after_id)

    def finalizar_splash():
        for after_id in pending_after_ids:
            try:
                splash_root.after_cancel(after_id)
            except Exception:
                pass
        splash.encerrar()
        estado["app"].iniciar()

    def carregar_em_segundo_plano():
        try:
            estado["app"] = Zeladoc_Application(progresso=progresso)
            splash_root.after(1500, finalizar_splash)
        except Exception:
            import traceback
            traceback.print_exc()
            splash_root.after(0, splash_root.destroy)

    threading.Thread(target=carregar_em_segundo_plano, daemon=True).start()
    splash_root.mainloop()


if __name__ == "__main__":
    iniciar_com_splash()