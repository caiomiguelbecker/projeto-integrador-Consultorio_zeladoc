from app.models.consulta import Consulta
from app.core.idioma import Idioma


class Consulta_controller:
    
    def __init__(self, dao, paciente_dao, medico_dao, view):
        self.dao = dao
        self.paciente_dao = paciente_dao
        self.medico_dao = medico_dao
        self.view = view
    
    def new(self):
        self.view.limpar_campos()
        
    def carregar_pacientes(self):
        pacientes = self.paciente_dao.listar()
        self.view.carregar_pacientes(pacientes)
    
    def carregar_medicos(self):
        medicos = self.medico_dao.listar()
        self.view.carregar_medicos(medicos)
    
    def save(self):
        try:
            data_hora, paciente, medico = self.view.get_dados()
            consulta = Consulta(
                None,
                data_hora,
                paciente,
                medico
            )
            self.dao.save(consulta)
            self.get_all()
            self.view.exibir_mensagem(Idioma.t("consulta.cadastrado_sucesso"))
        except ValueError as e:
            self.view.exibir_mensagem(f"{Idioma.t('comun.erro_prefixo')}: {str(e)}", False)
    
    def get_all(self):
        consultas = self.dao.get_all()
        self.view.exibir_consultas(consultas)        
    
    def selecionar_consulta(self, event):
        try:
            id_consulta = self.view.get_id_selecionado()
            self.consulta_selecionada = self.dao.get_by_id(id_consulta)
            self.view.preencher_campos(self.consulta_selecionada)
        except IndexError:
            pass
    
    def update(self):
        try:
            if self.consulta_selecionada is None:
                self.view.exibir_mensagem(Idioma.t("consulta.selecione_da_lista"), False)
                return
            data_hora, paciente, medico = self.view.ler_dados_consulta()
            self.consulta_selecionada.atualizar_dados(data_hora, paciente, medico)
            self.dao.update(self.consulta_selecionada)
            self.get_all()
            self.view.exibir_mensagem(Idioma.t("consulta.atualizado_sucesso"))
        except ValueError as e:
            self.view.exibir_mensagem(f"{Idioma.t('comun.erro_prefixo')}: {str(e)}", False)
        
    def delete(self):
        if self.consulta_selecionada is None:
            self.view.exibir_mensagem(Idioma.t("consulta.selecione_da_lista"), False)
            return
        if not self.view.confirmar_exclusao():
            return
        try:
            sucesso = self.dao.delete(self.consulta_selecionada.id)
            if sucesso:
                self.cidade_selecionada = None
                self.view.limpar_campos()
                self.get_all()
                self.view.exibir_mensagem(Idioma.t("consulta.excluido_sucesso"))
            else:
                self.view.exibir_mensagem(Idioma.t("consulta.nao_encontrado"), False)
        except ValueError as e:
            self.view.exibir_mensagem(Idioma.t("consulta.erro_excluir"), False)