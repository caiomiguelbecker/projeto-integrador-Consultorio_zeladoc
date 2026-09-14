import mysql.connector

from app.models.usuario import Usuario
from app.core.idioma import Idioma
from app.core.senha_utils import Senha_Utils

# AQUI NÃO ENTRARIA, PODEMOS DELETAR
# class Usuario_Controller:

#     def __init__(self, dao, view):
#         self.dao = dao
#         self.view = view
#         self.usuario_selecionado = None

#     def new(self):
#         self.view.limpar_campos()

class Usuario_Controller:

    def __init__(self, dao, view=None):
        self.dao = dao
        self.view = view
        self.usuario_selecionado = None

    def autenticar(self, email, senha):
        usuario = self.dao.get_by_email(email)

        if usuario is None:
            return None

        if not Senha_Utils.verificar_senha(senha, usuario.senha):
            return None

        return usuario

    def new(self):
        self.view.limpar_campos()

    def save(self):
        try:
            nome, email, senha = self.view.ler_dados_usuario()
            if not senha:
                raise ValueError("usuario.erro_senha_vazia")
            usuario = Usuario(None, nome, email, Senha_Utils.gerar_hash(senha))
            self.dao.save(usuario)
            self.get_all()
            self.view.exibir_mensagem(Idioma.t("usuario.cadastrado_sucesso"))
        except ValueError as e:
            self.view.exibir_mensagem(f"{Idioma.t('comum.erro_prefixo')}{Idioma.t(str(e))}", False)

    def get_all(self):
        usuarios = self.dao.get_all()
        self.view.exibir_usuarios(usuarios)

    def selecionar_usuario(self, event):
        try:
            id_usuario = self.view.get_id_selecionado()
            self.usuario_selecionado = self.dao.get_by_id(id_usuario)
            self.view.preencher_campos(self.usuario_selecionado)
        except IndexError:
            pass

    def update(self):
        try:
            if self.usuario_selecionado is None:
                self.view.exibir_mensagem(Idioma.t("usuario.selecione_da_lista"), False)
                return
            nome, email, senha = self.view.ler_dados_usuario()
            self.usuario_selecionado.atualizar_dados(nome, email)
            if senha:
                self.usuario_selecionado.senha = Senha_Utils.gerar_hash(senha)
            self.dao.update(self.usuario_selecionado)
            self.get_all()
            self.view.exibir_mensagem(Idioma.t("usuario.atualizado_sucesso"))
        except ValueError as e:
            self.view.exibir_mensagem(f"{Idioma.t('comum.erro_prefixo')}{Idioma.t(str(e))}", False)

    def delete(self):
        if self.usuario_selecionado is None:
            self.view.exibir_mensagem(Idioma.t("usuario.selecione_da_lista"), False)
            return
        if not self.view.confirmar_exclusao():
            return
        try:
            sucesso = self.dao.delete(self.usuario_selecionado.id)
            if sucesso:
                self.usuario_selecionado = None
                self.view.limpar_campos()
                self.get_all()
                self.view.exibir_mensagem(Idioma.t("usuario.excluido_sucesso"))
            else:
                self.view.exibir_mensagem(Idioma.t("usuario.nao_encontrado"), False)
        except mysql.connector.errors.IntegrityError:
            self.view.exibir_mensagem(Idioma.t("usuario.erro_possui_vinculos"), False)
        except Exception:
            self.view.exibir_mensagem(Idioma.t("usuario.erro_ao_excluir"), False)