from app.models.especialidade import Especialidade
from app.models.usuario import Usuario

class Medico:
    
    def __init__(self, id, nome, usuario: Usuario, especialidade: Especialidade):
        self._id = id
        self._nome = nome
        self._especialidade = especialidade
        self._usuario = usuario
        
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
            raise ValueError("medico.nome_vazio")
        self._nome = novo_nome
    
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
        
    def atualizar_dados(self, novo_nome, nova_especialidade, novo_usuario):
        self._nome = novo_nome
        self._especialidade = nova_especialidade
        self._usuario = novo_usuario