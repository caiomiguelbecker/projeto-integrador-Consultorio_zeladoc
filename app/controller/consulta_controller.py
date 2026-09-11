from app.models.consulta import Consulta
from app.core.data_utils import Data_Utils
from app.core.idioma import Idioma


class Consulta_Controller:

    def __init__(self, dao, paciente_dao, medico_dao, exame_dao, consulta_exame_dao, view):
        self.dao = dao
        self.paciente_dao = paciente_dao
        self.medico_dao = medico_dao
        self.exame_dao = exame_dao
        self.consulta_exame_dao = consulta_exame_dao
        self.view = view
        self.consulta_selecionada = None

    def new(self):
        self.consulta_selecionada = None
        self.view.limpar_campos()

    def carregar_pacientes(self):
        pacientes = self.paciente_dao.get_all()
        self.view.carregar_pacientes(pacientes)

    def carregar_medicos(self):
        medicos = self.medico_dao.get_all()
        self.view.carregar_medicos(medicos)

    def carregar_exames(self):
        exames = self.exame_dao.get_all()
        self.view.carregar_exames(exames)

    def save(self):
        try:
            data_hora, paciente, medico = self.view.ler_dados_consulta()

            if not Data_Utils.validar_data_hora(data_hora):
                raise ValueError("consulta.erro_data_invalida")

            consulta = Consulta(
                None,
                Data_Utils.string_para_data_hora(data_hora),
                paciente,
                medico
            )
            self.dao.save(consulta)
            self.get_all()
            self.view.exibir_mensagem(Idioma.t("consulta.cadastrado_sucesso"))
        except ValueError as e:
            self.view.exibir_mensagem(f"{Idioma.t('comum.erro_prefixo')}{Idioma.t(str(e))}", False)
        except Exception as e:
            self.view.exibir_mensagem(f"Erro ao salvar consulta: {e}", False)

    def get_all(self):
        try:
            consultas = self.dao.get_all()
            self.view.exibir_consultas(consultas)
        except Exception as e:
            self.view.exibir_mensagem(f"Erro ao carregar consultas: {e}", False)

    def selecionar_consulta(self, event):
        try:
            id_consulta = self.view.get_id_selecionado()
            self.consulta_selecionada = self.dao.get_by_id(id_consulta)
            self.view.preencher_campos(self.consulta_selecionada)
            self.carregar_exames_da_consulta()
        except IndexError:
            pass

    def carregar_exames_da_consulta(self):
        if self.consulta_selecionada is None:
            self.view.exibir_exames_consulta([])
            return
        exames = self.consulta_exame_dao.get_exames_by_consulta(self.consulta_selecionada.id)
        self.view.exibir_exames_consulta(exames)

    def adicionar_exame(self):
        if self.consulta_selecionada is None:
            self.view.exibir_mensagem(Idioma.t("consulta.erro_salve_consulta_primeiro"), False)
            return
        try:
            exame = self.view.get_exame_para_adicionar()
            self.consulta_exame_dao.adicionar(self.consulta_selecionada.id, exame.id)
            self.carregar_exames_da_consulta()
            self.view.exibir_mensagem(Idioma.t("consulta.exame_adicionado_sucesso"))
        except ValueError as e:
            self.view.exibir_mensagem(f"{Idioma.t('comum.erro_prefixo')}{Idioma.t(str(e))}", False)
        except Exception as e:
            self.view.exibir_mensagem(f"Erro ao adicionar exame: {e}", False)

    def remover_exame(self):
        if self.consulta_selecionada is None:
            self.view.exibir_mensagem(Idioma.t("consulta.erro_salve_consulta_primeiro"), False)
            return
        try:
            exame = self.view.get_exame_selecionado_para_remover()
            self.consulta_exame_dao.remover(self.consulta_selecionada.id, exame.id)
            self.carregar_exames_da_consulta()
            self.view.exibir_mensagem(Idioma.t("consulta.exame_removido_sucesso"))
        except ValueError as e:
            self.view.exibir_mensagem(f"{Idioma.t('comum.erro_prefixo')}{Idioma.t(str(e))}", False)
        except Exception as e:
            self.view.exibir_mensagem(f"Erro ao remover exame: {e}", False)

    def update(self):
        try:
            if self.consulta_selecionada is None:
                self.view.exibir_mensagem(Idioma.t("consulta.selecione_da_lista"), False)
                return

            data_hora, paciente, medico = self.view.ler_dados_consulta()

            if not Data_Utils.validar_data_hora(data_hora):
                raise ValueError("consulta.erro_data_invalida")

            self.consulta_selecionada.atualizar_dados(
                Data_Utils.string_para_data_hora(data_hora),
                paciente,
                medico
            )
            self.dao.update(self.consulta_selecionada)
            self.get_all()
            self.view.exibir_mensagem(Idioma.t("consulta.atualizado_sucesso"))
        except ValueError as e:
            self.view.exibir_mensagem(f"{Idioma.t('comum.erro_prefixo')}{Idioma.t(str(e))}", False)
        except Exception as e:
            self.view.exibir_mensagem(f"Erro ao atualizar consulta: {e}", False)

    def delete(self):
        if self.consulta_selecionada is None:
            self.view.exibir_mensagem(Idioma.t("consulta.selecione_da_lista"), False)
            return
        if not self.view.confirmar_exclusao():
            return
        try:
            sucesso = self.dao.delete(self.consulta_selecionada.id)
            if sucesso:
                self.consulta_selecionada = None
                self.view.limpar_campos()
                self.get_all()
                self.view.exibir_mensagem(Idioma.t("consulta.excluido_sucesso"))
            else:
                self.view.exibir_mensagem(Idioma.t("consulta.nao_encontrado"), False)
        except Exception as e:
            self.view.exibir_mensagem(f"Erro ao excluir consulta: {e}", False)