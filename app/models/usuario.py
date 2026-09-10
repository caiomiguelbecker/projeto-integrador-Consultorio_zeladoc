class Usuario:

    def __init__(self, id, nome, email, senha):
        self.id = id
        self.nome = nome
        self.email = email
        self._senha = senha

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, novo_id):
        self._id = novo_id

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        if not novo_nome or not novo_nome.strip():
            raise ValueError("usuario.erro_nome_vazio")
        self._nome = novo_nome

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, novo_email):
        if not novo_email or not novo_email.strip():
            raise ValueError("usuario.erro_email_vazio")
        self._email = novo_email

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, nova_senha):
        self._senha = nova_senha

    def atualizar_dados(self, novo_nome, novo_email):
        self.nome = novo_nome
        self.email = novo_email

    def __str__(self):
        return self.nome