from app.models.exame import Exame
from app.core.idioma import Idioma


class Exame_Controller:

    def __init__(self, dao, view):
        self.dao = dao
        self.view = view
        self.exame_selecionado = None

    def new(self):
        self.view.limpar_campos()

    def save(self):
        try:
            nome = self.view.ler_dados_exame()
            exame = Exame(None, nome)
            self.dao.save(exame)
            self.get_all()
            self.view.exibir_mensagem(Idioma.t("exame.cadastrado_sucesso"))
        except ValueError as e:
            self.view.exibir_mensagem(f"{Idioma.t('comum.erro_prefixo')}{Idioma.t(str(e))}", False)

    def get_all(self):
        exames = self.dao.get_all()
        self.view.exibir_exames(exames)

    def selecionar_exame(self, event):
        try:
            id_exame = self.view.get_id_selecionado()
            self.exame_selecionado = self.dao.get_by_id(id_exame)
            self.view.preencher_campos(self.exame_selecionado)
        except IndexError:
            pass

    def update(self):
        try:
            if self.exame_selecionado is None:
                self.view.exibir_mensagem(Idioma.t("exame.selecione_da_lista"), False)
                return
            nome = self.view.ler_dados_exame()
            self.exame_selecionado.atualizar_dados(nome)
            self.dao.update(self.exame_selecionado)
            self.get_all()
            self.view.exibir_mensagem(Idioma.t("exame.atualizado_sucesso"))
        except ValueError as e:
            self.view.exibir_mensagem(f"{Idioma.t('comum.erro_prefixo')}{Idioma.t(str(e))}", False)

    def delete(self):
        if self.exame_selecionado is None:
            self.view.exibir_mensagem(Idioma.t("exame.selecione_da_lista"), False)
            return
        if not self.view.confirmar_exclusao():
            return
        try:
            sucesso = self.dao.delete(self.exame_selecionado.id)
            if sucesso:
                self.exame_selecionado = None
                self.view.limpar_campos()
                self.get_all()
                self.view.exibir_mensagem(Idioma.t("exame.excluido_sucesso"))
            else:
                self.view.exibir_mensagem(Idioma.t("exame.nao_encontrado"), False)
        except Exception:
            self.view.exibir_mensagem(Idioma.t("exame.erro_ao_excluir"), False)