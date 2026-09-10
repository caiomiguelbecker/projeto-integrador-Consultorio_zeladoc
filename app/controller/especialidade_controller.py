import mysql.connector

from app.models.especialidade import Especialidade
from app.core.idioma import Idioma


class Especialidade_Controller:

    def __init__(self, dao, view):
        self.dao = dao
        self.view = view
        self.especialidade_selecionada = None

    def new(self):
        self.view.limpar_campos()

    def save(self):
        try:
            nome = self.view.ler_dados_especialidade()
            especialidade = Especialidade(None, nome)
            self.dao.save(especialidade)
            self.get_all()
            self.view.exibir_mensagem(Idioma.t("especialidade.cadastrado_sucesso"))
        except ValueError as e:
            self.view.exibir_mensagem(f"{Idioma.t('comum.erro_prefixo')}{Idioma.t(str(e))}", False)

    def get_all(self):
        especialidades = self.dao.get_all()
        self.view.exibir_especialidades(especialidades)

    def selecionar_especialidade(self, event):
        try:
            id_especialidade = self.view.get_id_selecionado()
            self.especialidade_selecionada = self.dao.get_by_id(id_especialidade)
            self.view.preencher_campos(self.especialidade_selecionada)
        except IndexError:
            pass

    def update(self):
        try:
            if self.especialidade_selecionada is None:
                self.view.exibir_mensagem(Idioma.t("especialidade.selecione_da_lista"), False)
                return
            nome = self.view.ler_dados_especialidade()
            self.especialidade_selecionada.atualizar_dados(nome)
            self.dao.update(self.especialidade_selecionada)
            self.get_all()
            self.view.exibir_mensagem(Idioma.t("especialidade.atualizado_sucesso"))
        except ValueError as e:
            self.view.exibir_mensagem(f"{Idioma.t('comum.erro_prefixo')}{Idioma.t(str(e))}", False)

    def delete(self):
        if self.especialidade_selecionada is None:
            self.view.exibir_mensagem(Idioma.t("especialidade.selecione_da_lista"), False)
            return
        if not self.view.confirmar_exclusao():
            return
        try:
            sucesso = self.dao.delete(self.especialidade_selecionada.id)
            if sucesso:
                self.especialidade_selecionada = None
                self.view.limpar_campos()
                self.get_all()
                self.view.exibir_mensagem(Idioma.t("especialidade.excluido_sucesso"))
            else:
                self.view.exibir_mensagem(Idioma.t("especialidade.nao_encontrado"), False)
        except mysql.connector.errors.IntegrityError:
            self.view.exibir_mensagem(Idioma.t("especialidade.erro_possui_vinculos"), False)
        except Exception:
            self.view.exibir_mensagem(Idioma.t("especialidade.erro_ao_excluir"), False)