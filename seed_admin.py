import getpass

from app.core.database import Database
from app.core.senha_utils import Senha_Utils
from app.dao.usuario_dao import Usuario_DAO
from app.models.usuario import Usuario


def criar_usuario_inicial(usuario_dao, nome, email, senha):
    if usuario_dao.get_all():
        return None

    usuario = Usuario(
        None,
        nome,
        email,
        Senha_Utils.gerar_hash(senha)
    )

    return usuario_dao.save(usuario)


def main():
    database = Database()
    usuario_dao = Usuario_DAO(database)

    if usuario_dao.get_all():
        print("Já existem usuários cadastrados. Seed não é necessário.")
        return

    print("=== Criação do usuário administrador inicial ===")
    nome = input("Nome: ").strip()
    email = input("E-mail: ").strip()
    senha = getpass.getpass("Senha: ")

    if not nome or not email or not senha:
        print("Nome, e-mail e senha são obrigatórios. Seed cancelado.")
        return

    usuario = criar_usuario_inicial(usuario_dao, nome, email, senha)

    if usuario is None:
        print("Já existem usuários cadastrados. Seed não é necessário.")
        return

    print()
    print(f"Usuário criado com sucesso: {usuario.email}")
    print("Já pode fazer login na aplicação com essas credenciais.")


if __name__ == "__main__":
    main()