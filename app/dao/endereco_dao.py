from app.dao.dao import DAO
from app.dao.paciente_dao import Paciente_DAO
from app.models.endereco import Endereco

class Endereco_DAO(DAO):

    def __init__(self, database):
        super().__init__(database)
        self._paciente_dao = Paciente_DAO(database)
        
    def save(self, Endereco):
        
        cursor, conexao = self.conectar()
        
        try:
            
            sql =   """
                        INSERT INTO ENDERECO
                            (
                            LOGRADOURO,
                            NUMERO,
                            CIDADE,
                            UF,
                            ID_PACIENTE
                            )
                        VALUES
                        (
                            %s,
                            %s,
                            %s,
                            %s,
                            %s
                        )                    
                    """
            cursor.execute(
                sql,
                (
                    Endereco.logradouro,
                    Endereco.numero,
                    Endereco.cidade,
                    Endereco.uf,
                    Endereco.paciente.id
                )
                )
            
            conexao.commit()
            
            Endereco.id = cursor.lastrowid
            return Endereco
        
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
                            LOGRADOURO,
                            NUMERO,
                            CIDADE,
                            UF,
                            ID_PACIENTE
                        FROM
                            ENDERECO
                        ORDER BY
                            CIDADE                        
                    """
            cursor.execute(sql)
            
            registros = cursor.fetchall()
            enderecos = []
            
            for registro in registros:
                
                enderecos.append(
                    Endereco(
                    registro[0],
                    registro[1],
                    registro[2],
                    registro[3],
                    registro[4],
                    self._paciente_dao.get_by_id(registro[5])
                    )
                )
            return enderecos
        
        finally:
                
                self.desconectar(cursor, conexao)
                
    def get_by_id(self, id):
        
        cursor, conexao = self.conectar()
        
        try:
            sql =  """
                        SELECT 
                            ID,
                            LOGRADOURO,
                            NUMERO,
                            CIDADE,
                            UF,
                            ID_PACIENTE
                        FROM
                            ENDERECO
                        WHERE
                            ID = %s
                    """
            cursor.execute(sql, (id,))
            registro = cursor.fetchone()
            
            if registro is None:
                return None
            
            return Endereco(
                registro[0],
                registro[1],
                registro[2],
                registro[3],
                registro[4],
                self._paciente_dao.get_by_id(registro[5])
            )
            
        finally:
                
                self.desconectar(cursor, conexao)
                
    def update(self, Endereco):
        
        cursor, conexao = self.conectar()
        
        try:
            sql =   """
                        UPDATE ENDERECO
                        SET
                            LOGRADOURO = %s,
                            NUMERO = %s,
                            CIDADE = %s,
                            UF = %s,
                            ID_PACIENTE = %s
                        WHERE
                            ID = %s
                    """
            cursor.execute(
                sql,
                (
                    Endereco.logradouro,
                    Endereco.numero,
                    Endereco.cidade,
                    Endereco.uf,
                    Endereco.paciente.id,
                    Endereco.id
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
                        DELETE FROM ENDERECO
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
                    