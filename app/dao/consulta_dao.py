from app.dao.dao import DAO
from app.models.consulta import Consulta

class Consulta_DAO(DAO):
    
    def __init__(self, database, Paciente_DAO, Medico_DAO):
        super().__init__(database)
        self._Paciente_DAO = Paciente_DAO
        self._Medico_DAO = Medico_DAO
        
    def save(self, Consulta):
        
        cursor, conexao = self.conectar()
        
        try:
            
            sql =   """
                        INSET INTO CONSULTA 
                            (
                            DATA_HORA,
                            ID_PACIENTE,
                            ID_MEDICO
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
                    Consulta.data_hora,
                    Consulta.id_paciente,
                    Consulta.id_medico
                )
                )
            
            conexao.commit()
            
            Consulta.id = cursor.lastrowid
                
            return Consulta
    
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
                            DATA_HORA,
                            ID_PACIENTE,
                            ID_MEDICO
                        FROM 
                            CONSULTA
                        ORDER BY
                            DATA_HORA
                    """
            cursor.execute(sql)
            
            registros = cursor.fetchall()
            consultas = []
            
            for registro in registros:
                paciente = self._Paciente_DAO.get_by_id(
                    registro[2]
                    )
                medico = self._Medico_DAO.get_by_id(
                    registro[3]
                    )
                consultas.append(
                    Consulta(
                        registro[0],
                        registro[1],
                        paciente,
                        medico
                    )
                )
            return consultas
        
        finally:
            
            self.desconectar(cursor, conexao)
    
    def get_by_paciente(self, id_paciente):
        
        cursor, conexao = self.conectar()
        
        try:
            sql =   """
                    SELECT
                        ID,
                        NOME,
                        ID_PACIENTE
                    FROM
                        PACIENTE
                    ORDER BY 
                        NOME                                           
                    """
            cursor.execute(
                sql,
                (id_paciente,)
            )
            registros = cursor.fetchall()
            consultas = []
            for registro in registros:
                paciente = self._Paciente_DAO.get_by_id(
                    registro[2]
                    )
                medico = self._Medico_DAO.get_by_id(
                    registro[3]
                    )
                consultas.append(
                    Consulta(
                        registro[0],
                        registro[1],
                        paciente,
                        medico
                    )
                )
            return consultas
        finally:
            
            self.desconectar(cursor, conexao)
    
    def get_by_medico(self, id_medico):
        
        cursor, conexao = self.conectar()
        
        try:
            sql =   """
                    SELECT
                        ID,
                        NOME,
                        ID_MEDICO
                    FROM
                        MEDICO
                    ORDER BY 
                        NOME                                           
                    """
            cursor.execute(
                sql,
                (id_medico,)
            )
            registros = cursor.fetchall()
            consultas = []
            for registro in registros:
                paciente = self._Paciente_DAO.get_by_id(
                    registro[2]
                    )
                medico = self._Medico_DAO.get_by_id(
                    registro[3]
                    )
                consultas.append(
                    Consulta(
                        registro[0],
                        registro[1],
                        paciente,
                        medico
                    )
                )
            return consultas
        finally:
            
            self.desconectar(cursor, conexao)
    
    def get_by_id(self, id):
        
        cursor, conexao = self.conectar()
        
        try:
            sql =   """
                        SELECT
                            ID,
                            DATA_HORA,
                            ID_PACIENTE,
                            ID_MEDICO
                        FROM 
                            CONSULTA
                        WHERE
                            ID = %s
                    """
                    
            cursor.execute(sql,(id,))
            registro = cursor.fetchone()
            
            if registro is None:
                return None
            
            paciente = self._Paciente_DAO.get_by_id(
                registro[2]
                )
            medico = self._Medico_DAO.get_by_id(
                registro[3]
                )
            
            return Consulta(
                registro[0],
                registro[1],
                paciente,
                medico
            )
            
        finally:
            
            self.desconectar(cursor, conexao)
            
    def update(self, Consulta):
        
        cursor, conexao = self.conectar()
        
        try:
            
            sql =   """
                        UPDATE CONSULTA
                        SET
                            DATA_HORA = %s,
                            ID_PACIENTE = %s,
                            ID_MEDICO = %s
                        WHERE
                            ID = %s
                    """
            cursor.execute(
                sql,
                (
                    Consulta.data_hora,
                    Consulta.id_paciente,
                    Consulta.id_medico,
                    Consulta.id
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
                        DELETE FROM CONSULTA
                        WHERE ID = %s
                    """
            cursor.execute(sql,(id,))
            
            conexao.commit()
            
            return cursor.rowcount > 0
        
        except Exception:
            
            conexao.rollback()
            raise
        
        finally:
            
            self.desconectar(cursor, conexao)
    