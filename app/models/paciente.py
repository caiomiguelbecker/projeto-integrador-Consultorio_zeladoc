from app.models.convenio import Convenio
from app.models.endereco import Endereco
from app.core.data_utils import Data_Utils


class Paciente:

    def __init__(self, id, nome, data_nascimento, convenio: Convenio = None, endereco: Endereco = None):
        self.id = id
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.convenio = convenio
        self.endereco = endereco

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, novo_id):
        self._id = novo_id

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        if not novo_nome or not novo_nome.strip():
            raise ValueError("paciente.erro_nome_vazio")
        self._nome = novo_nome

    @property
    def data_nascimento(self):
        return self._data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, nova_data_nascimento):
        self._data_nascimento = nova_data_nascimento

    @property
    def convenio(self):
        return self._convenio

    @convenio.setter
    def convenio(self, novo_convenio):
        self._convenio = novo_convenio

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, novo_endereco):
        self._endereco = novo_endereco

    @property
    def idade(self):
        return Data_Utils.calcular_idade(self._data_nascimento)

    def atualizar_dados(self, novo_nome, nova_data_nascimento, novo_convenio, novo_endereco):
        self.nome = novo_nome
        self.data_nascimento = nova_data_nascimento
        self.convenio = novo_convenio
        self.endereco = novo_endereco

    def __str__(self):
        return self.nome