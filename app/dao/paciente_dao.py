from app.dao.dao import DAO
from app.models.paciente import Paciente
from app.models.endereco import Endereco


class Paciente_DAO(DAO):

    def __init__(self, database, convenio_dao):
        super().__init__(database)
        self._convenio_dao = convenio_dao

    def save(self, paciente):

        conexao, cursor = self.conectar()

        try:
            sql = """
                    INSERT INTO paciente
                        (nome, data_nascimento, id_convenio)
                    VALUES
                        (%s, %s, %s)
                  """

            id_convenio = paciente.convenio.id if paciente.convenio else None

            cursor.execute(
                sql,
                (paciente.nome, paciente.data_nascimento, id_convenio)
            )

            paciente.id = cursor.lastrowid

            if paciente.endereco is not None:
                sql_endereco = """
                        INSERT INTO endereco
                            (logradouro, numero, cidade, uf, id_paciente)
                        VALUES
                            (%s, %s, %s, %s, %s)
                      """
                cursor.execute(
                    sql_endereco,
                    (
                        paciente.endereco.logradouro,
                        paciente.endereco.numero,
                        paciente.endereco.cidade,
                        paciente.endereco.uf,
                        paciente.id
                    )
                )
                paciente.endereco.id = cursor.lastrowid

            conexao.commit()

            return paciente

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
                        p.id_paciente,
                        p.nome,
                        p.data_nascimento,
                        p.id_convenio,
                        e.id_endereco,
                        e.logradouro,
                        e.numero,
                        e.cidade,
                        e.uf
                    FROM
                        paciente p
                    LEFT JOIN
                        endereco e ON e.id_paciente = p.id_paciente
                    ORDER BY
                        p.nome
                  """

            cursor.execute(sql)

            registros = cursor.fetchall()

            return [self._montar_paciente(registro) for registro in registros]

        finally:
            self.desconectar(cursor, conexao)

    def get_by_id(self, id):

        conexao, cursor = self.conectar()

        try:
            sql = """
                    SELECT
                        p.id_paciente,
                        p.nome,
                        p.data_nascimento,
                        p.id_convenio,
                        e.id_endereco,
                        e.logradouro,
                        e.numero,
                        e.cidade,
                        e.uf
                    FROM
                        paciente p
                    LEFT JOIN
                        endereco e ON e.id_paciente = p.id_paciente
                    WHERE
                        p.id_paciente = %s
                  """

            cursor.execute(sql, (id,))

            registro = cursor.fetchone()

            if registro is None:
                return None

            return self._montar_paciente(registro)

        finally:
            self.desconectar(cursor, conexao)

    def _montar_paciente(self, registro):
        convenio = self._convenio_dao.get_by_id(registro[3]) if registro[3] else None

        endereco = None
        if registro[4] is not None:
            endereco = Endereco(registro[4], registro[5], registro[6], registro[7], registro[8])

        return Paciente(registro[0], registro[1], registro[2], convenio, endereco)

    def update(self, paciente):

        conexao, cursor = self.conectar()

        try:
            sql = """
                    UPDATE paciente
                    SET
                        nome = %s,
                        data_nascimento = %s,
                        id_convenio = %s
                    WHERE
                        id_paciente = %s
                  """

            id_convenio = paciente.convenio.id if paciente.convenio else None

            cursor.execute(
                sql,
                (paciente.nome, paciente.data_nascimento, id_convenio, paciente.id)
            )

            if paciente.endereco is not None:
                if paciente.endereco.id is None:
                    sql_endereco = """
                            INSERT INTO endereco
                                (logradouro, numero, cidade, uf, id_paciente)
                            VALUES
                                (%s, %s, %s, %s, %s)
                          """
                    cursor.execute(
                        sql_endereco,
                        (
                            paciente.endereco.logradouro,
                            paciente.endereco.numero,
                            paciente.endereco.cidade,
                            paciente.endereco.uf,
                            paciente.id
                        )
                    )
                    paciente.endereco.id = cursor.lastrowid
                else:
                    sql_endereco = """
                            UPDATE endereco
                            SET
                                logradouro = %s,
                                numero = %s,
                                cidade = %s,
                                uf = %s
                            WHERE
                                id_endereco = %s
                          """
                    cursor.execute(
                        sql_endereco,
                        (
                            paciente.endereco.logradouro,
                            paciente.endereco.numero,
                            paciente.endereco.cidade,
                            paciente.endereco.uf,
                            paciente.endereco.id
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
            # Remove primeiro os registros que dependem do paciente
            # (consulta e prontuario têm FOREIGN KEY para paciente),
            # senão o MySQL recusa a exclusão com erro de restrição.
            cursor.execute("DELETE FROM prontuario WHERE id_paciente = %s", (id,))
            cursor.execute("DELETE FROM consulta WHERE id_paciente = %s", (id,))
            cursor.execute("DELETE FROM endereco WHERE id_paciente = %s", (id,))
            cursor.execute("DELETE FROM paciente WHERE id_paciente = %s", (id,))

            conexao.commit()

            return cursor.rowcount > 0

        except Exception:
            conexao.rollback()
            raise

        finally:
            self.desconectar(cursor, conexao)