from app.models.paciente import Paciente

class Endereco:
    
    def __init__ (self, id, logradouro, numero, cidade, uf, paciente: Paciente):
        self._id = id
        self._lougradouro = logradouro
        self._numero = numero
        self._cidade = cidade
        self._uf = uf
        self._paciente = paciente
        
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, novo_id):
        self._id = novo_id
    
    @property
    def logradouro(self):
        return self._lougradouro
    
    @logradouro.setter
    def logradouro(self, novo_logradouro):
        self._lougradouro = novo_logradouro
        
    @property
    def numero(self):
        return self._numero
    
    @numero.setter
    def numero(self, novo_numero):
        self._numero = novo_numero
        
    @property
    def cidade(self):
        return self._cidade
    
    @cidade.setter
    def cidade(self, nova_cidade):
        self._cidade = nova_cidade
        
    @property
    def uf(self):
        return self._uf
    
    @uf.setter
    def uf(self, nova_uf):
        self._uf = nova_uf
        
    @property
    def paciente(self):
        return self._paciente
    
    @paciente.setter
    def paciente(self, novo_paciente: Paciente):
        self._paciente = novo_paciente
        
    def atualizar_dados(self, novo_logradouro, novo_numero, nova_cidade, nova_uf):
        self._lougradouro = novo_logradouro
        self._numero = novo_numero
        self._cidade = nova_cidade
        self._uf = nova_uf