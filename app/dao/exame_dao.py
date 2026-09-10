from app.dao.dao import DAO
from app.models.exame import Exame


class Exame_DAO(DAO):

    def __init__(self, database):
        super().__init__(database)

    def save(self, exame):

        conexao, cursor = self.conectar()

        try:
            sql = """
                    INSERT INTO exame
                        (nome_exame)
                    VALUES
                        (%s)
                  """

            cursor.execute(sql, (exame.nome,))

            conexao.commit()

            exame.id = cursor.lastrowid

            return exame

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
                        id_exame,
                        nome_exame
                    FROM
                        exame
                    ORDER BY
                        nome_exame
                  """

            cursor.execute(sql)

            registros = cursor.fetchall()

            return [Exame(registro[0], registro[1]) for registro in registros]

        finally:
            self.desconectar(cursor, conexao)

    def get_by_id(self, id):

        conexao, cursor = self.conectar()

        try:
            sql = """
                    SELECT
                        id_exame,
                        nome_exame
                    FROM
                        exame
                    WHERE
                        id_exame = %s
                  """

            cursor.execute(sql, (id,))

            registro = cursor.fetchone()

            if registro is None:
                return None

            return Exame(registro[0], registro[1])

        finally:
            self.desconectar(cursor, conexao)

    def update(self, exame):

        conexao, cursor = self.conectar()

        try:
            sql = """
                    UPDATE exame
                    SET
                        nome_exame = %s
                    WHERE
                        id_exame = %s
                  """

            cursor.execute(sql, (exame.nome, exame.id))

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
                    DELETE FROM exame
                    WHERE id_exame = %s
                  """

            cursor.execute(sql, (id,))

            conexao.commit()

            return cursor.rowcount > 0

        except Exception:
            conexao.rollback()
            raise

        finally:
            self.desconectar(cursor, conexao)