from app.models.paciente import Paciente
from app.models.endereco import Endereco
from app.core.data_utils import Data_Utils
from app.core.idioma import Idioma


class Paciente_Controller:

    def __init__(self, dao, convenio_dao, view):
        self.dao = dao
        self.convenio_dao = convenio_dao
        self.view = view
        self.paciente_selecionado = None

    def new(self):
        self.view.limpar_campos()

    def carregar_convenios(self):
        convenios = self.convenio_dao.get_all()
        self.view.carregar_convenios(convenios)

    def save(self):
        try:
            (
                nome,
                data_nascimento,
                convenio,
                logradouro,
                numero,
                cidade,
                uf
            ) = self.view.ler_dados_paciente()

            if not Data_Utils.validar_data(data_nascimento):
                raise ValueError("paciente.erro_data_invalida")

            endereco = Endereco(None, logradouro, self._converter_numero(numero), cidade, uf)

            paciente = Paciente(
                None,
                nome,
                Data_Utils.string_para_data(data_nascimento),
                convenio,
                endereco
            )
            self.dao.save(paciente)
            self.get_all()
            self.view.exibir_mensagem(Idioma.t("paciente.cadastrado_sucesso"))
        except ValueError as e:
            self.view.exibir_mensagem(f"{Idioma.t('comum.erro_prefixo')}{Idioma.t(str(e))}", False)

    def get_all(self):
        pacientes = self.dao.get_all()
        self.view.exibir_pacientes(pacientes)

    def selecionar_paciente(self, event):
        try:
            id_paciente = self.view.get_id_selecionado()
            self.paciente_selecionado = self.dao.get_by_id(id_paciente)
            self.view.preencher_campos(self.paciente_selecionado)
        except IndexError:
            pass

    def update(self):
        try:
            if self.paciente_selecionado is None:
                self.view.exibir_mensagem(Idioma.t("paciente.selecione_da_lista"), False)
                return

            (
                nome,
                data_nascimento,
                convenio,
                logradouro,
                numero,
                cidade,
                uf
            ) = self.view.ler_dados_paciente()

            if not Data_Utils.validar_data(data_nascimento):
                raise ValueError("paciente.erro_data_invalida")

            endereco_atual = self.paciente_selecionado.endereco
            id_endereco = endereco_atual.id if endereco_atual else None
            endereco = Endereco(id_endereco, logradouro, self._converter_numero(numero), cidade, uf)

            self.paciente_selecionado.atualizar_dados(
                nome,
                Data_Utils.string_para_data(data_nascimento),
                convenio,
                endereco
            )
            self.dao.update(self.paciente_selecionado)
            self.get_all()
            self.view.exibir_mensagem(Idioma.t("paciente.atualizado_sucesso"))
        except ValueError as e:
            self.view.exibir_mensagem(f"{Idioma.t('comum.erro_prefixo')}{Idioma.t(str(e))}", False)

    def delete(self):
        if self.paciente_selecionado is None:
            self.view.exibir_mensagem(Idioma.t("paciente.selecione_da_lista"), False)
            return
        if not self.view.confirmar_exclusao():
            return
        try:
            sucesso = self.dao.delete(self.paciente_selecionado.id)
            if sucesso:
                self.paciente_selecionado = None
                self.view.limpar_campos()
                self.get_all()
                self.view.exibir_mensagem(Idioma.t("paciente.excluido_sucesso"))
            else:
                self.view.exibir_mensagem(Idioma.t("paciente.nao_encontrado"), False)
        except Exception:
            self.view.exibir_mensagem(Idioma.t("paciente.erro_ao_excluir"), False)

    def _converter_numero(self, numero):
        try:
            return int(numero)
        except (TypeError, ValueError):
            raise ValueError("paciente.erro_numero_invalido")