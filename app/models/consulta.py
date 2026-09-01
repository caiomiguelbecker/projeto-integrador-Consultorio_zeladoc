from app.models.medico import Medico
from app.models.paciente import Paciente

class Consulta:
    
    def __init__(self, id, data_hora,paciente: Paciente, medico: Medico):
        self._id = id
        self._data_hora = data_hora
        self._paciente = paciente
        self._medico = medico
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, novo_id):
        self._id = novo_id
    
    @property
    def data_hora(self):
        return self._data_hora
    
    @data_hora.setter
    def data_hora(self, nova_data_hora):
        self._data_hora = nova_data_hora
    
    @property
    def paciente(self):
        return self._paciente
    
    @paciente.setter
    def paciente(self, novo_paciente):
        self._paciente = novo_paciente
        
    @property
    def medico(self):
        return self._medico
    
    @medico.setter
    def medico(self, novo_medico):
        self._medico = novo_medico
        
    def atualizar_dados(self,novo_data_hora, novo_paciente, novo_medico):
        self._data_hora = novo_data_hora
        self._paciente = novo_paciente
        self._medico = novo_medico