from app.dao.dao import DAO
from app.models.convenio import Convenio


class Convenio_DAO(DAO):

    def __init__(self, database):
        super().__init__(database)

    def save(self, convenio):

        conexao, cursor = self.conectar()

        try:
            sql = """
                    INSERT INTO convenio
                        (nome)
                    VALUES
                        (%s)
                  """

            cursor.execute(sql, (convenio.nome,))

            conexao.commit()

            convenio.id = cursor.lastrowid

            return convenio

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
                        id_convenio,
                        nome
                    FROM
                        convenio
                    ORDER BY
                        nome
                  """

            cursor.execute(sql)

            registros = cursor.fetchall()

            return [Convenio(registro[0], registro[1]) for registro in registros]

        finally:
            self.desconectar(cursor, conexao)

    def get_by_id(self, id):

        conexao, cursor = self.conectar()

        try:
            sql = """
                    SELECT
                        id_convenio,
                        nome
                    FROM
                        convenio
                    WHERE
                        id_convenio = %s
                  """

            cursor.execute(sql, (id,))

            registro = cursor.fetchone()

            if registro is None:
                return None

            return Convenio(registro[0], registro[1])

        finally:
            self.desconectar(cursor, conexao)

    def update(self, convenio):

        conexao, cursor = self.conectar()

        try:
            sql = """
                    UPDATE convenio
                    SET
                        nome = %s
                    WHERE
                        id_convenio = %s
                  """

            cursor.execute(sql, (convenio.nome, convenio.id))

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
                    DELETE FROM convenio
                    WHERE id_convenio = %s
                  """

            cursor.execute(sql, (id,))

            conexao.commit()

            return cursor.rowcount > 0

        except Exception:
            conexao.rollback()
            raise

        finally:
            self.desconectar(cursor, conexao)