from app.dao.dao import DAO
from app.models.usuario import Usuario


class Usuario_DAO(DAO):

    def __init__(self, database):
        super().__init__(database)

    def save(self, usuario):

        conexao, cursor = self.conectar()

        try:
            sql = """
                    INSERT INTO usuario
                        (nome_usuario, email, senha)
                    VALUES
                        (%s, %s, %s)
                  """

            cursor.execute(
                sql,
                (usuario.nome, usuario.email, usuario.senha)
            )

            conexao.commit()

            usuario.id = cursor.lastrowid

            return usuario

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
                        id_usuario,
                        nome_usuario,
                        email,
                        senha
                    FROM
                        usuario
                    ORDER BY
                        nome_usuario
                  """

            cursor.execute(sql)

            registros = cursor.fetchall()

            return [
                Usuario(registro[0], registro[1], registro[2], registro[3])
                for registro in registros
            ]

        finally:
            self.desconectar(cursor, conexao)

    def get_by_id(self, id):

        conexao, cursor = self.conectar()

        try:
            sql = """
                    SELECT
                        id_usuario,
                        nome_usuario,
                        email,
                        senha
                    FROM
                        usuario
                    WHERE
                        id_usuario = %s
                  """

            cursor.execute(sql, (id,))

            registro = cursor.fetchone()

            if registro is None:
                return None

            return Usuario(registro[0], registro[1], registro[2], registro[3])

        finally:
            self.desconectar(cursor, conexao)

    def get_by_email(self, email):

        conexao, cursor = self.conectar()

        try:
            sql = """
                    SELECT
                        id_usuario,
                        nome_usuario,
                        email,
                        senha
                    FROM
                        usuario
                    WHERE
                        email = %s
                  """

            cursor.execute(sql, (email,))

            registro = cursor.fetchone()

            if registro is None:
                return None

            return Usuario(registro[0], registro[1], registro[2], registro[3])

        finally:
            self.desconectar(cursor, conexao)

    def update(self, usuario):

        conexao, cursor = self.conectar()

        try:
            sql = """
                    UPDATE usuario
                    SET
                        nome_usuario = %s,
                        email = %s,
                        senha = %s
                    WHERE
                        id_usuario = %s
                  """

            cursor.execute(
                sql,
                (usuario.nome, usuario.email, usuario.senha, usuario.id)
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
                    DELETE FROM usuario
                    WHERE id_usuario = %s
                  """

            cursor.execute(sql, (id,))

            conexao.commit()

            return cursor.rowcount > 0

        except Exception:
            conexao.rollback()
            raise

        finally:
            self.desconectar(cursor, conexao)