from app.dao.dao import DAO
from app.models.usuario import Usuario

class Usuario_DAO(DAO):

    def __init__(self, database):
        super().__init__(database)
        
    def save(self, Usuario):
        
        cursor, conexao = self.conectar()
        
        try:
            
            sql =   """
                        INSERT INTO USUARIO
                            (
                            NOME,
                            EMAIL,
                            SENHA
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
                    Usuario.nome,
                    Usuario.email,
                    Usuario.senha
                )
                )
            
            conexao.commit()
            
            Usuario.id = cursor.lastrowid
            return Usuario
        
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
                            EMAIL,
                            SENHA
                        FROM
                            USUARIO
                        ORDER BY
                            NOME                        
                    """
            cursor.execute(sql)
            
            registros = cursor.fetchall()
            usuarios = []
            
            for registro in registros:
                
                usuarios.append(
                    Usuario(
                    registro[0],
                    registro[1],
                    registro[2],
                    registro[3]
                    )
                )
            return usuarios
        
        finally:
                
                self.desconectar(cursor, conexao)
                
    def get_by_id(self, id):
        
        cursor, conexao = self.conectar()
        
        try:
            sql =  """
                        SELECT 
                            ID,
                            NOME,
                            EMAIL,
                            SENHA
                        FROM
                            USUARIO
                        WHERE
                            ID = %s
                    """
            cursor.execute(sql, (id,))
            registro = cursor.fetchone()
            
            if registro is None:
                return None
            
            return Usuario(
                registro[0],
                registro[1],
                registro[2],
                registro[3]
            )
            
        finally:
                
                self.desconectar(cursor, conexao)
                
    def update(self, Usuario):
        
        cursor, conexao = self.conectar()
        
        try:
            sql =   """
                        UPDATE USUARIO
                        SET
                            NOME = %s,
                            EMAIL = %s,
                            SENHA = %s
                        WHERE
                            ID = %s
                    """
            cursor.execute(
                sql,
                (
                    Usuario.nome,
                    Usuario.email,
                    Usuario.senha,
                    Usuario.id
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
                        DELETE FROM USUARIO
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