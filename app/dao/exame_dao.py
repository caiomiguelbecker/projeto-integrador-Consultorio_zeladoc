from app.dao.dao import DAO
from app.models.exame import Exame

class Exame_DAO(DAO):

    def __init__(self, database):
        super().__init__(database)
        
    def save(self, Exame):
        
        cursor, conexao = self.conectar()
        
        try:
            
            sql =   """
                        INSERT INTO EXAME
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
                    Exame.nome,
                )
                )
            
            conexao.commit()
            
            Exame.id = cursor.lastrowid
            return Exame
        
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
                            EXAME
                        ORDER BY
                            NOME                        
                    """
            cursor.execute(sql)
            
            registros = cursor.fetchall()
            exames = []
            
            for registro in registros:
                
                exames.append(
                    Exame(
                    registro[0],
                    registro[1]
                    )
                )
            return exames
        
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
                            EXAME
                        WHERE
                            ID = %s
                    """
            cursor.execute(sql, (id,))
            registro = cursor.fetchone()
            
            if registro is None:
                return None
            
            return Exame(
                registro[0],
                registro[1]
            )
            
        finally:
                
                self.desconectar(cursor, conexao)
                
    def update(self, Exame):
        
        cursor, conexao = self.conectar()
        
        try:
            sql =   """
                        UPDATE EXAME
                        SET
                            NOME = %s
                        WHERE
                            ID = %s
                    """
            cursor.execute(
                sql,
                (
                    Exame.nome,
                    Exame.id
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
                        DELETE FROM EXAME
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

