class Endereco:

    def __init__(self, id, logradouro, numero, cidade, uf):
        self.id = id
        self.logradouro = logradouro
        self.numero = numero
        self.cidade = cidade
        self.uf = uf

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, novo_id):
        self._id = novo_id

    @property
    def logradouro(self):
        return self._logradouro

    @logradouro.setter
    def logradouro(self, novo_logradouro):
        self._logradouro = novo_logradouro

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, novo_numero):
        self._numero = novo_numero

    @property
    def cidade(self):
        return self._cidade

    @cidade.setter
    def cidade(self, nova_cidade):
        self._cidade = nova_cidade

    @property
    def uf(self):
        return self._uf

    @uf.setter
    def uf(self, nova_uf):
        self._uf = nova_uf

    def atualizar_dados(self, novo_logradouro, novo_numero, nova_cidade, nova_uf):
        self.logradouro = novo_logradouro
        self.numero = novo_numero
        self.cidade = nova_cidade
        self.uf = nova_uf