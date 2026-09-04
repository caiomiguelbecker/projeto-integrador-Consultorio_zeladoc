from app.dao.dao import DAO
from app.models.convenio import Convenio

class Convenio_DAO(DAO):

    def __init__(self, database):
        super().__init__(database)
        
    def save(self, Convenio):
        
        cursor, conexao = self.conectar()
        
        try:
            
            sql =   """
                        INSERT INTO CONVENIO
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
                    Convenio.nome,
                )
                )
            
            conexao.commit()
            
            Convenio.id = cursor.lastrowid
            return Convenio
        
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
                            CONVENIO
                        ORDER BY
                            NOME                        
                    """
            cursor.execute(sql)
            
            registros = cursor.fetchall()
            convenios = []
            
            for registro in registros:
                
                convenios.append(
                    Convenio(
                    registro[0],
                    registro[1]
                    )
                )
            return convenios
        
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
                            CONVENIO
                        WHERE
                            ID = %s
                    """
            cursor.execute(sql, (id,))
            registro = cursor.fetchone()
            
            if registro is None:
                return None
            
            return Convenio(
                registro[0],
                registro[1]
            )
            
        finally:
                
                self.desconectar(cursor, conexao)
                
    def update(self, Convenio):
        
        cursor, conexao = self.conectar()
        
        try:
            sql =   """
                        UPDATE CONVENIO
                        SET
                            NOME = %s
                        WHERE
                            ID = %s
                    """
            cursor.execute(
                sql,
                (
                    Convenio.nome,
                    Convenio.id
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
                        DELETE FROM CONVENIO
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