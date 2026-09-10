from app.dao.dao import DAO
from app.dao.especialidade_dao import Especialidade_DAO
from app.dao.usuario_dao import Usuario_DAO
from app.models.medico import Medico

class Medico_DAO(DAO):

    def __init__(self, database):
        super().__init__(database)
        self._especialidade_dao = Especialidade_DAO(database)
        self._usuario_dao = Usuario_DAO(database)
        
    def save(self, Medico):
        
        cursor, conexao = self.conectar()
        
        try:
            
            sql =   """
                        INSERT INTO MEDICO
                            (
                            NOME,
                            ID_ESPECIALIDADE,
                            ID_USUARIO
                            )
                        VALUES
                        (
                            %s,
                            %s,
                            %s
                        )                    
                    """
            cursor.execute(
                sql,
                (
                    Medico.nome,
                    Medico.especialidade.id,
                    Medico.usuario.id
                )
                )
            
            conexao.commit()
            
            Medico.id = cursor.lastrowid
            return Medico
        
        except Exception:
                
                conexao.rollback()
                raise
        finally:
                
                self.desconectar(cursor, conexao)
                
    def get_all(self):
         
        cursor, conexao = self.conectar()
         
        try:
             
            sql =   """
                        SELECT 
                            ID,
                            NOME,
                            ID_ESPECIALIDADE,
                            ID_USUARIO
                        FROM
                            MEDICO
                        ORDER BY
                            NOME                        
                    """
            cursor.execute(sql)
            
            registros = cursor.fetchall()
            medicos = []
            
            for registro in registros:
                
                medicos.append(
                    Medico(
                    registro[0],
                    registro[1],
                    self._usuario_dao.get_by_id(registro[3]),
                    self._especialidade_dao.get_by_id(registro[2])
                    )
                )
            return medicos
        
        finally:
                
                self.desconectar(cursor, conexao)
                
    def get_by_id(self, id):
        
        cursor, conexao = self.conectar()
        
        try:
            sql =  """
                        SELECT 
                            ID,
                            NOME,
                            ID_ESPECIALIDADE,
                            ID_USUARIO
                        FROM
                            MEDICO
                        WHERE
                            ID = %s
                    """
            cursor.execute(sql, (id,))
            registro = cursor.fetchone()
            
            if registro is None:
                return None
            
            return Medico(
                registro[0],
                registro[1],
                self._usuario_dao.get_by_id(registro[3]),
                self._especialidade_dao.get_by_id(registro[2])
            )
            
        finally:
                
                self.desconectar(cursor, conexao)
                
    def update(self, Medico):
        
        cursor, conexao = self.conectar()
        
        try:
            sql =   """
                        UPDATE MEDICO
                        SET
                            NOME = %s,
                            ID_ESPECIALIDADE = %s,
                            ID_USUARIO = %s
                        WHERE
                            ID = %s
                    """
            cursor.execute(
                sql,
                (
                    Medico.nome,
                    Medico.especialidade.id,
                    Medico.usuario.id,
                    Medico.id
                )
            )
            
            conexao.commit()
            
            return cursor.rowcount > 0
        
        except Exception:
                
                conexao.rollback()
                raise
        finally:
                
                self.desconectar(cursor, conexao)  
    
    
    def delete(self, id):
        
        cursor, conexao = self.conectar()
        
        try: 
            sql =   """
                        DELETE FROM MEDICO
                        WHERE ID = %s         
                    """
            
            cursor.execute(sql, (id,))
            conexao.commit()
            return cursor.rowcount > 0
        
        except Exception:
                
                conexao.rollback()
                raise
        
        finally:
                    
                    self.desconectar(cursor, conexao)
                    
