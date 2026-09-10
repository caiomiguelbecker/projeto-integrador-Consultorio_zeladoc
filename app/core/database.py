import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


class Database:
    def conectar(self):
        return mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", ""),
            database=os.getenv("DB_NAME", "zeladoc")
        )

    def desconectar(self, cursor, conexao):
        cursor.close()
        conexao.close()