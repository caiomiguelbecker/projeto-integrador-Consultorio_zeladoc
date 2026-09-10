import mysql.connector

from app.models.convenio import Convenio
from app.core.idioma import Idioma


class Convenio_Controller:

    def __init__(self, dao, view):
        self.dao = dao
        self.view = view
        self.convenio_selecionado = None

    def new(self):
        self.view.limpar_campos()

    def save(self):
        try:
            nome = self.view.ler_dados_convenio()
            convenio = Convenio(None, nome)
            self.dao.save(convenio)
            self.get_all()
            self.view.exibir_mensagem(Idioma.t("convenio.cadastrado_sucesso"))
        except ValueError as e:
            self.view.exibir_mensagem(f"{Idioma.t('comum.erro_prefixo')}{Idioma.t(str(e))}", False)

    def get_all(self):
        convenios = self.dao.get_all()
        self.view.exibir_convenios(convenios)

    def selecionar_convenio(self, event):
        try:
            id_convenio = self.view.get_id_selecionado()
            self.convenio_selecionado = self.dao.get_by_id(id_convenio)
            self.view.preencher_campos(self.convenio_selecionado)
        except IndexError:
            pass

    def update(self):
        try:
            if self.convenio_selecionado is None:
                self.view.exibir_mensagem(Idioma.t("convenio.selecione_da_lista"), False)
                return
            nome = self.view.ler_dados_convenio()
            self.convenio_selecionado.atualizar_dados(nome)
            self.dao.update(self.convenio_selecionado)
            self.get_all()
            self.view.exibir_mensagem(Idioma.t("convenio.atualizado_sucesso"))
        except ValueError as e:
            self.view.exibir_mensagem(f"{Idioma.t('comum.erro_prefixo')}{Idioma.t(str(e))}", False)

    def delete(self):
        if self.convenio_selecionado is None:
            self.view.exibir_mensagem(Idioma.t("convenio.selecione_da_lista"), False)
            return
        if not self.view.confirmar_exclusao():
            return
        try:
            sucesso = self.dao.delete(self.convenio_selecionado.id)
            if sucesso:
                self.convenio_selecionado = None
                self.view.limpar_campos()
                self.get_all()
                self.view.exibir_mensagem(Idioma.t("convenio.excluido_sucesso"))
            else:
                self.view.exibir_mensagem(Idioma.t("convenio.nao_encontrado"), False)
        except mysql.connector.errors.IntegrityError:
            self.view.exibir_mensagem(Idioma.t("convenio.erro_possui_vinculos"), False)
        except Exception:
            self.view.exibir_mensagem(Idioma.t("convenio.erro_ao_excluir"), False)