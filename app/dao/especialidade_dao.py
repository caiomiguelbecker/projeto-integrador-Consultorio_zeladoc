from app.dao.dao import DAO
from app.models.especialidade import Especialidade

class Especialidade_DAO(DAO):

    def __init__(self, database):
        super().__init__(database)
        
    def save(self, Especialidade):
        
        cursor, conexao = self.conectar()
        
        try:
            
            sql =   """
                        INSERT INTO ESPECIALIDADE
                            (
                            NOME
                            )
                        VALUES
                        (
                            %s
                        )                    
                    """
            cursor.execute(
                sql,
                (
                    Especialidade.nome,
                )
                )
            
            conexao.commit()
            
            Especialidade.id = cursor.lastrowid
            return Especialidade
        
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
                            NOME
                        FROM
                            ESPECIALIDADE
                        ORDER BY
                            NOME                        
                    """
            cursor.execute(sql)
            
            registros = cursor.fetchall()
            especialidades = []
            
            for registro in registros:
                
                especialidades.append(
                    Especialidade(
                    registro[0],
                    registro[1]
                    )
                )
            return especialidades
        
        finally:
                
                self.desconectar(cursor, conexao)
                
    def get_by_id(self, id):
        
        cursor, conexao = self.conectar()
        
        try:
            sql =  """
                        SELECT 
                            ID,
                            NOME
                        FROM
                            ESPECIALIDADE
                        WHERE
                            ID = %s
                    """
            cursor.execute(sql, (id,))
            registro = cursor.fetchone()
            
            if registro is None:
                return None
            
            return Especialidade(
                registro[0],
                registro[1]
            )
            
        finally:
                
                self.desconectar(cursor, conexao)
                
    def update(self, Especialidade):
        
        cursor, conexao = self.conectar()
        
        try:
            sql =   """
                        UPDATE ESPECIALIDADE
                        SET
                            NOME = %s
                        WHERE
                            ID = %s
                    """
            cursor.execute(
                sql,
                (
                    Especialidade.nome,
                    Especialidade.id
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
                        DELETE FROM ESPECIALIDADE
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
