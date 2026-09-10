from app.dao.dao import DAO
from app.models.consulta import Consulta


class Consulta_DAO(DAO):

    def __init__(self, database, paciente_dao, medico_dao):
        super().__init__(database)
        self._paciente_dao = paciente_dao
        self._medico_dao = medico_dao

    def save(self, consulta):

        conexao, cursor = self.conectar()

        try:
            sql = """
                    INSERT INTO consulta
                        (data_hora, id_paciente, id_medico)
                    VALUES
                        (%s, %s, %s)
                  """

            cursor.execute(
                sql,
                (consulta.data_hora, consulta.paciente.id, consulta.medico.id)
            )

            conexao.commit()

            consulta.id = cursor.lastrowid

            return consulta

        except Exception:
            conexao.rollback()
            raise

        finally:
            self.desconectar(cursor, conexao)

    def get_all(self):

        conexao, cursor = self.conectar()

        try:
            sql = """
                    SELECT
                        id_consulta,
                        data_hora,
                        id_paciente,
                        id_medico
                    FROM
                        consulta
                    ORDER BY
                        data_hora
                  """

            cursor.execute(sql)

            registros = cursor.fetchall()

            return [self._montar_consulta(registro) for registro in registros]

        finally:
            self.desconectar(cursor, conexao)

    def get_by_id(self, id):

        conexao, cursor = self.conectar()

        try:
            sql = """
                    SELECT
                        id_consulta,
                        data_hora,
                        id_paciente,
                        id_medico
                    FROM
                        consulta
                    WHERE
                        id_consulta = %s
                  """

            cursor.execute(sql, (id,))

            registro = cursor.fetchone()

            if registro is None:
                return None

            return self._montar_consulta(registro)

        finally:
            self.desconectar(cursor, conexao)

    def get_by_paciente(self, id_paciente):

        conexao, cursor = self.conectar()

        try:
            sql = """
                    SELECT
                        id_consulta,
                        data_hora,
                        id_paciente,
                        id_medico
                    FROM
                        consulta
                    WHERE
                        id_paciente = %s
                    ORDER BY
                        data_hora
                  """

            cursor.execute(sql, (id_paciente,))

            registros = cursor.fetchall()

            return [self._montar_consulta(registro) for registro in registros]

        finally:
            self.desconectar(cursor, conexao)

    def get_by_medico(self, id_medico):

        conexao, cursor = self.conectar()

        try:
            sql = """
                    SELECT
                        id_consulta,
                        data_hora,
                        id_paciente,
                        id_medico
                    FROM
                        consulta
                    WHERE
                        id_medico = %s
                    ORDER BY
                        data_hora
                  """

            cursor.execute(sql, (id_medico,))

            registros = cursor.fetchall()

            return [self._montar_consulta(registro) for registro in registros]

        finally:
            self.desconectar(cursor, conexao)

    def _montar_consulta(self, registro):
        paciente = self._paciente_dao.get_by_id(registro[2])
        medico = self._medico_dao.get_by_id(registro[3])
        return Consulta(registro[0], registro[1], paciente, medico)

    def update(self, consulta):

        conexao, cursor = self.conectar()

        try:
            sql = """
                    UPDATE consulta
                    SET
                        data_hora = %s,
                        id_paciente = %s,
                        id_medico = %s
                    WHERE
                        id_consulta = %s
                  """

            cursor.execute(
                sql,
                (
                    consulta.data_hora,
                    consulta.paciente.id,
                    consulta.medico.id,
                    consulta.id
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

        conexao, cursor = self.conectar()

        try:
            sql = """
                    DELETE FROM consulta
                    WHERE id_consulta = %s
                  """

            cursor.execute(sql, (id,))

            conexao.commit()

            return cursor.rowcount > 0

        except Exception:
            conexao.rollback()
            raise

        finally:
            self.desconectar(cursor, conexao)