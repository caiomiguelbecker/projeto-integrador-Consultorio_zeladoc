from app.dao.dao import DAO
from app.models.especialidade import Especialidade


class Especialidade_DAO(DAO):

    def __init__(self, database):
        super().__init__(database)

    def save(self, especialidade):

        conexao, cursor = self.conectar()

        try:
            sql = """
                    INSERT INTO especialidades
                        (nome_especialidade)
                    VALUES
                        (%s)
                  """

            cursor.execute(sql, (especialidade.nome,))

            conexao.commit()

            especialidade.id = cursor.lastrowid

            return especialidade

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
                        id_especialidade,
                        nome_especialidade
                    FROM
                        especialidades
                    ORDER BY
                        nome_especialidade
                  """

            cursor.execute(sql)

            registros = cursor.fetchall()

            return [Especialidade(registro[0], registro[1]) for registro in registros]

        finally:
            self.desconectar(cursor, conexao)

    def get_by_id(self, id):

        conexao, cursor = self.conectar()

        try:
            sql = """
                    SELECT
                        id_especialidade,
                        nome_especialidade
                    FROM
                        especialidades
                    WHERE
                        id_especialidade = %s
                  """

            cursor.execute(sql, (id,))

            registro = cursor.fetchone()

            if registro is None:
                return None

            return Especialidade(registro[0], registro[1])

        finally:
            self.desconectar(cursor, conexao)

    def update(self, especialidade):

        conexao, cursor = self.conectar()

        try:
            sql = """
                    UPDATE especialidades
                    SET
                        nome_especialidade = %s
                    WHERE
                        id_especialidade = %s
                  """

            cursor.execute(sql, (especialidade.nome, especialidade.id))

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
                    DELETE FROM especialidades
                    WHERE id_especialidade = %s
                  """

            cursor.execute(sql, (id,))

            conexao.commit()

            return cursor.rowcount > 0

        except Exception:
            conexao.rollback()
            raise

        finally:
            self.desconectar(cursor, conexao)