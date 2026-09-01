class Especialidade:
    
    def __init__(self, id, nome):
        self._id = id
        self._nome = nome
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, novo_id):
        self._id = novo_id
        
    @property
    def nome(self):
        return self._nome.upper()
    
    @nome.setter
    def nome(self, novo_nome):
        if not novo_nome or not novo_nome.strip():
            raise ValueError("especialidade.nome_vazio")
        self._nome = novo_nome
        
    def atualizar_dados(self, novo_nome):
        self._nome = novo_nome
    
    
    
    
        