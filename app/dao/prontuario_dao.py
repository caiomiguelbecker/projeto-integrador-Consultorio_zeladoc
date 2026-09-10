from app.dao.dao import DAO
from app.models.prontuario import Prontuario


class Prontuario_DAO(DAO):

    def __init__(self, database, paciente_dao):
        super().__init__(database)
        self._paciente_dao = paciente_dao

    def save(self, prontuario):

        conexao, cursor = self.conectar()

        try:
            sql = """
                    INSERT INTO prontuario
                        (observacoes, id_paciente)
                    VALUES
                        (%s, %s)
                  """

            cursor.execute(
                sql,
                (prontuario.observacoes, prontuario.paciente.id)
            )

            conexao.commit()

            prontuario.id = cursor.lastrowid

            return prontuario

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
                        id_prontuario,
                        observacoes,
                        id_paciente
                    FROM
                        prontuario
                    ORDER BY
                        id_prontuario
                  """

            cursor.execute(sql)

            registros = cursor.fetchall()

            return [self._montar_prontuario(registro) for registro in registros]

        finally:
            self.desconectar(cursor, conexao)

    def get_by_id(self, id):

        conexao, cursor = self.conectar()

        try:
            sql = """
                    SELECT
                        id_prontuario,
                        observacoes,
                        id_paciente
                    FROM
                        prontuario
                    WHERE
                        id_prontuario = %s
                  """

            cursor.execute(sql, (id,))

            registro = cursor.fetchone()

            if registro is None:
                return None

            return self._montar_prontuario(registro)

        finally:
            self.desconectar(cursor, conexao)

    def get_by_paciente(self, id_paciente):

        conexao, cursor = self.conectar()

        try:
            sql = """
                    SELECT
                        id_prontuario,
                        observacoes,
                        id_paciente
                    FROM
                        prontuario
                    WHERE
                        id_paciente = %s
                    ORDER BY
                        id_prontuario
                  """

            cursor.execute(sql, (id_paciente,))

            registros = cursor.fetchall()

            return [self._montar_prontuario(registro) for registro in registros]

        finally:
            self.desconectar(cursor, conexao)

    def _montar_prontuario(self, registro):
        paciente = self._paciente_dao.get_by_id(registro[2])
        return Prontuario(registro[0], registro[1], paciente)

    def update(self, prontuario):

        conexao, cursor = self.conectar()

        try:
            sql = """
                    UPDATE prontuario
                    SET
                        observacoes = %s,
                        id_paciente = %s
                    WHERE
                        id_prontuario = %s
                  """

            cursor.execute(
                sql,
                (prontuario.observacoes, prontuario.paciente.id, prontuario.id)
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
                    DELETE FROM prontuario
                    WHERE id_prontuario = %s
                  """

            cursor.execute(sql, (id,))

            conexao.commit()

            return cursor.rowcount > 0

        except Exception:
            conexao.rollback()
            raise

        finally:
            self.desconectar(cursor, conexao)