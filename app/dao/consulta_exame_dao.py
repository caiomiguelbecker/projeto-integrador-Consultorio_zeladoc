from app.models.exame import Exame


class Consulta_Exame_DAO:
    def __init__(self, database):
        self._database = database

    def conectar(self):
        conexao = self._database.conectar()
        cursor = conexao.cursor()
        return conexao, cursor

    def desconectar(self, cursor, conexao):
        self._database.desconectar(cursor, conexao)

    def adicionar(self, id_consulta, id_exame):

        conexao, cursor = self.conectar()

        try:
            cursor.execute(
                """
                SELECT 1
                FROM consulta_exame
                WHERE id_consulta = %s AND id_exame = %s
                """,
                (id_consulta, id_exame)
            )

            if cursor.fetchone() is not None:
                raise ValueError("consulta.erro_exame_ja_vinculado")

            cursor.execute(
                """
                INSERT INTO consulta_exame (id_consulta, id_exame)
                VALUES (%s, %s)
                """,
                (id_consulta, id_exame)
            )

            conexao.commit()

        except ValueError:
            conexao.rollback()
            raise

        except Exception:
            conexao.rollback()
            raise

        finally:
            self.desconectar(cursor, conexao)

    def remover(self, id_consulta, id_exame):

        conexao, cursor = self.conectar()

        try:
            sql = """
                    DELETE FROM consulta_exame
                    WHERE id_consulta = %s AND id_exame = %s
                  """

            cursor.execute(sql, (id_consulta, id_exame))

            conexao.commit()

            return cursor.rowcount > 0

        except Exception:
            conexao.rollback()
            raise

        finally:
            self.desconectar(cursor, conexao)

    def remover_todos_da_consulta(self, id_consulta):
        """Usado quando a própria consulta é excluída."""

        conexao, cursor = self.conectar()

        try:
            cursor.execute(
                "DELETE FROM consulta_exame WHERE id_consulta = %s",
                (id_consulta,)
            )

            conexao.commit()

        except Exception:
            conexao.rollback()
            raise

        finally:
            self.desconectar(cursor, conexao)

    def get_exames_by_consulta(self, id_consulta):

        conexao, cursor = self.conectar()

        try:
            sql = """
                    SELECT
                        e.id_exame,
                        e.nome_exame
                    FROM
                        consulta_exame ce
                    JOIN
                        exame e ON e.id_exame = ce.id_exame
                    WHERE
                        ce.id_consulta = %s
                    ORDER BY
                        e.nome_exame
                  """

            cursor.execute(sql, (id_consulta,))

            registros = cursor.fetchall()

            return [Exame(registro[0], registro[1]) for registro in registros]

        finally:
            self.desconectar(cursor, conexao)