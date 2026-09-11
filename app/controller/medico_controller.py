from app.models.medico import Medico
from app.core.idioma import Idioma


class Medico_Controller:

    def __init__(self, dao, especialidade_dao, usuario_dao, view):
        self.dao = dao
        self.especialidade_dao = especialidade_dao
        self.usuario_dao = usuario_dao
        self.view = view
        self.medico_selecionado = None

    def new(self):
        self.view.limpar_campos()

    def carregar_especialidades(self):
        especialidades = self.especialidade_dao.get_all()
        self.view.carregar_especialidades(especialidades)

    def carregar_usuarios(self):
        usuarios = self.usuario_dao.get_all()
        self.view.carregar_usuarios(usuarios)

    def save(self):
        try:
            nome, crm, especialidade, usuario = self.view.ler_dados_medico()
            medico = Medico(None, nome, crm, especialidade, usuario)
            self.dao.save(medico)
            self.get_all()
            self.view.exibir_mensagem(Idioma.t("medico.cadastrado_sucesso"))
        except ValueError as e:
            self.view.exibir_mensagem(f"{Idioma.t('comum.erro_prefixo')}{Idioma.t(str(e))}", False)
        except Exception as e:
            self.view.exibir_mensagem(f"Erro ao salvar médico: {e}", False)

    def get_all(self):
        try:
            medicos = self.dao.get_all()
            self.view.exibir_medicos(medicos)
        except Exception as e:
            self.view.exibir_mensagem(f"Erro ao carregar médicos: {e}", False)

    def selecionar_medico(self, event):
        try:
            id_medico = self.view.get_id_selecionado()
            self.medico_selecionado = self.dao.get_by_id(id_medico)
            self.view.preencher_campos(self.medico_selecionado)
        except IndexError:
            pass

    def update(self):
        try:
            if self.medico_selecionado is None:
                self.view.exibir_mensagem(Idioma.t("medico.selecione_da_lista"), False)
                return
            nome, crm, especialidade, usuario = self.view.ler_dados_medico()
            self.medico_selecionado.atualizar_dados(nome, crm, especialidade, usuario)
            self.dao.update(self.medico_selecionado)
            self.get_all()
            self.view.exibir_mensagem(Idioma.t("medico.atualizado_sucesso"))
        except ValueError as e:
            self.view.exibir_mensagem(f"{Idioma.t('comum.erro_prefixo')}{Idioma.t(str(e))}", False)
        except Exception as e:
            self.view.exibir_mensagem(f"Erro ao atualizar médico: {e}", False)

    def delete(self):
        if self.medico_selecionado is None:
            self.view.exibir_mensagem(Idioma.t("medico.selecione_da_lista"), False)
            return
        if not self.view.confirmar_exclusao():
            return
        try:
            sucesso = self.dao.delete(self.medico_selecionado.id)
            if sucesso:
                self.medico_selecionado = None
                self.view.limpar_campos()
                self.get_all()
                self.view.exibir_mensagem(Idioma.t("medico.excluido_sucesso"))
            else:
                self.view.exibir_mensagem(Idioma.t("medico.nao_encontrado"), False)
        except Exception:
            self.view.exibir_mensagem(Idioma.t("medico.erro_ao_excluir"), False)