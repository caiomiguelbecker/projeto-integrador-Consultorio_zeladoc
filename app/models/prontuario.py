from app.models.paciente import Paciente


class Prontuario:

    def __init__(self, id, observacoes, paciente: Paciente):
        self.id = id
        self.observacoes = observacoes
        self.paciente = paciente

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, novo_id):
        self._id = novo_id

    @property
    def observacoes(self):
        return self._observacoes

    @observacoes.setter
    def observacoes(self, novas_observacoes):
        if not novas_observacoes or not novas_observacoes.strip():
            raise ValueError("prontuario.erro_observacoes_vazias")
        self._observacoes = novas_observacoes

    @property
    def paciente(self):
        return self._paciente

    @paciente.setter
    def paciente(self, novo_paciente):
        self._paciente = novo_paciente

    def atualizar_dados(self, novas_observacoes, novo_paciente):
        self.observacoes = novas_observacoes
        self.paciente = novo_paciente