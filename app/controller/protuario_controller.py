from app.models.prontuario import Prontuario
from app.core.idioma import Idioma


class Prontuario_Controller:

    def __init__(self, dao, paciente_dao, view):
        self.dao = dao
        self.paciente_dao = paciente_dao
        self.view = view
        self.prontuario_selecionado = None

    def new(self):
        self.view.limpar_campos()

    def carregar_pacientes(self):
        pacientes = self.paciente_dao.get_all()
        self.view.carregar_pacientes(pacientes)

    def save(self):
        try:
            observacoes, paciente = self.view.ler_dados_prontuario()
            prontuario = Prontuario(None, observacoes, paciente)
            self.dao.save(prontuario)
            self.get_all()
            self.view.exibir_mensagem(Idioma.t("prontuario.cadastrado_sucesso"))
        except ValueError as e:
            self.view.exibir_mensagem(f"{Idioma.t('comum.erro_prefixo')}{Idioma.t(str(e))}", False)

    def get_all(self):
        prontuarios = self.dao.get_all()
        self.view.exibir_prontuarios(prontuarios)

    def selecionar_prontuario(self, event):
        try:
            id_prontuario = self.view.get_id_selecionado()
            self.prontuario_selecionado = self.dao.get_by_id(id_prontuario)
            self.view.preencher_campos(self.prontuario_selecionado)
        except IndexError:
            pass

    def update(self):
        try:
            if self.prontuario_selecionado is None:
                self.view.exibir_mensagem(Idioma.t("prontuario.selecione_da_lista"), False)
                return
            observacoes, paciente = self.view.ler_dados_prontuario()
            self.prontuario_selecionado.atualizar_dados(observacoes, paciente)
            self.dao.update(self.prontuario_selecionado)
            self.get_all()
            self.view.exibir_mensagem(Idioma.t("prontuario.atualizado_sucesso"))
        except ValueError as e:
            self.view.exibir_mensagem(f"{Idioma.t('comum.erro_prefixo')}{Idioma.t(str(e))}", False)

    def delete(self):
        if self.prontuario_selecionado is None:
            self.view.exibir_mensagem(Idioma.t("prontuario.selecione_da_lista"), False)
            return
        if not self.view.confirmar_exclusao():
            return
        try:
            sucesso = self.dao.delete(self.prontuario_selecionado.id)
            if sucesso:
                self.prontuario_selecionado = None
                self.view.limpar_campos()
                self.get_all()
                self.view.exibir_mensagem(Idioma.t("prontuario.excluido_sucesso"))
            else:
                self.view.exibir_mensagem(Idioma.t("prontuario.nao_encontrado"), False)
        except Exception:
            self.view.exibir_mensagem(Idioma.t("prontuario.erro_ao_excluir"), False)