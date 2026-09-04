from abc import ABC,abstractmethod

class DAO(ABC):
    
    def __init__(self, database):
        self.database = database
        
    def conectar(self):
        conexao = self.database.conectar()
        cursor = conexao.cursor()
        return cursor, conexao
    
    def desconectar(self, cursor, conexao):
        self._database.desconectar(cursor, conexao)
        
    @abstractmethod
    def save(self, objeto):
        pass
    
    @abstractmethod
    def get_all(self):
        pass
    
    @abstractmethod
    def get_by_id(self, id):
        pass
    
    @abstractmethod
    def delete(self, id):
        pass