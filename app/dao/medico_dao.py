from app.dao.dao import DAO
from app.models.medico import Medico


class Medico_DAO(DAO):

    def __init__(self, database, especialidade_dao, usuario_dao):
        super().__init__(database)
        self._especialidade_dao = especialidade_dao
        self._usuario_dao = usuario_dao

    def save(self, medico):

        conexao, cursor = self.conectar()

        try:
            sql = """
                    INSERT INTO medico
                        (nome_medico, crm, id_especialidade, id_usuario)
                    VALUES
                        (%s, %s, %s, %s)
                  """

            cursor.execute(
                sql,
                (
                    medico.nome,
                    medico.crm,
                    medico.especialidade.id,
                    medico.usuario.id
                )
            )

            conexao.commit()

            medico.id = cursor.lastrowid

            return medico

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
                        id_medico,
                        nome_medico,
                        crm,
                        id_especialidade,
                        id_usuario
                    FROM
                        medico
                    ORDER BY
                        nome_medico
                  """

            cursor.execute(sql)

            registros = cursor.fetchall()

            return [self._montar_medico(registro) for registro in registros]

        finally:
            self.desconectar(cursor, conexao)

    def get_by_id(self, id):

        conexao, cursor = self.conectar()

        try:
            sql = """
                    SELECT
                        id_medico,
                        nome_medico,
                        crm,
                        id_especialidade,
                        id_usuario
                    FROM
                        medico
                    WHERE
                        id_medico = %s
                  """

            cursor.execute(sql, (id,))

            registro = cursor.fetchone()

            if registro is None:
                return None

            return self._montar_medico(registro)

        finally:
            self.desconectar(cursor, conexao)

    def _montar_medico(self, registro):
        especialidade = self._especialidade_dao.get_by_id(registro[3])
        usuario = self._usuario_dao.get_by_id(registro[4])
        return Medico(registro[0], registro[1], registro[2], especialidade, usuario)

    def update(self, medico):

        conexao, cursor = self.conectar()

        try:
            sql = """
                    UPDATE medico
                    SET
                        nome_medico = %s,
                        crm = %s,
                        id_especialidade = %s,
                        id_usuario = %s
                    WHERE
                        id_medico = %s
                  """

            cursor.execute(
                sql,
                (
                    medico.nome,
                    medico.crm,
                    medico.especialidade.id,
                    medico.usuario.id,
                    medico.id
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
            # Remove primeiro as consultas desse médico
            # (consulta tem FOREIGN KEY para medico).
            cursor.execute("DELETE FROM consulta WHERE id_medico = %s", (id,))

            sql = """
                    DELETE FROM medico
                    WHERE id_medico = %s
                  """

            cursor.execute(sql, (id,))

            conexao.commit()

            return cursor.rowcount > 0

        except Exception:
            conexao.rollback()
            raise

        finally:
            self.desconectar(cursor, conexao)