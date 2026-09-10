from app.models.especialidade import Especialidade
from app.models.usuario import Usuario


class Medico:

    def __init__(self, id, nome, crm, especialidade: Especialidade, usuario: Usuario):
        self.id = id
        self.nome = nome
        self.crm = crm
        self.especialidade = especialidade
        self.usuario = usuario

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
            raise ValueError("medico.erro_nome_vazio")
        self._nome = novo_nome

    @property
    def crm(self):
        return self._crm

    @crm.setter
    def crm(self, novo_crm):
        if not novo_crm or not novo_crm.strip():
            raise ValueError("medico.erro_crm_vazio")
        self._crm = novo_crm

    @property
    def especialidade(self):
        return self._especialidade

    @especialidade.setter
    def especialidade(self, nova_especialidade):
        self._especialidade = nova_especialidade

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, novo_usuario):
        self._usuario = novo_usuario

    def atualizar_dados(self, novo_nome, novo_crm, nova_especialidade, novo_usuario):
        self.nome = novo_nome
        self.crm = novo_crm
        self.especialidade = nova_especialidade
        self.usuario = novo_usuario

    def __str__(self):
        return self.nome