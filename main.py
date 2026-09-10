import ttkbootstrap as ttk

from app.core.database import Database

from app.dao.convenio_dao import Convenio_DAO
from app.dao.especialidade_dao import Especialidade_DAO
from app.dao.exame_dao import Exame_DAO
from app.dao.usuario_dao import Usuario_DAO
from app.dao.medico_dao import Medico_DAO
from app.dao.paciente_dao import Paciente_DAO
from app.dao.consulta_dao import Consulta_DAO
from app.dao.prontuario_dao import Prontuario_DAO

from app.views.menu_principal import Menu_Principal


class Zeladoc_Application:

    def __init__(self):
        self.database = Database()
        self.daos = self._criar_daos()

    def _criar_daos(self):
        convenio_dao = Convenio_DAO(self.database)
        especialidade_dao = Especialidade_DAO(self.database)
        exame_dao = Exame_DAO(self.database)
        usuario_dao = Usuario_DAO(self.database)
        medico_dao = Medico_DAO(self.database, especialidade_dao, usuario_dao)
        paciente_dao = Paciente_DAO(self.database, convenio_dao)
        consulta_dao = Consulta_DAO(self.database, paciente_dao, medico_dao)
        prontuario_dao = Prontuario_DAO(self.database, paciente_dao)

        return {
            "convenio": convenio_dao,
            "especialidade": especialidade_dao,
            "exame": exame_dao,
            "usuario": usuario_dao,
            "medico": medico_dao,
            "paciente": paciente_dao,
            "consulta": consulta_dao,
            "prontuario": prontuario_dao,
        }

    def iniciar(self):
        root = ttk.Window(themename="flatly")
        Menu_Principal(root, self.daos)
        root.mainloop()


if __name__ == "__main__":
    app = Zeladoc_Application()
    app.iniciar()