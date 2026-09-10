from datetime import datetime, date
from app.core.idioma import Idioma

class Data_Utils:

    @staticmethod
    def formato_atual():
        return "%d/%m/%Y" if Idioma.ATUAL == "pt" else "%m/%d/Y"

    @staticmethod
    def string_para_data(data):
        return datetime.strptime(data,Data_Utils.formato_atual()).date()
    
    @staticmethod
    def data_para_string(data):
        return data.strftime(Data_Utils.formato_atual())
    
    @staticmethod
    def validar_data(data):
        try:
            datetime.strptime(data, Data_Utils.formato_atual())
            return True
        except ValueError:
            return False
        
    @staticmethod
    def calcular_idade(data):
        data_inicio = data
        if isinstance(data, str):
            data_inicio = Data_Utils.string_para_data(data)
        elif not isinstance(data, date):
            raise ValueError("Formato de data inválido.")
        hoje = date.today()
        idade = hoje.year - data_inicio.year
        if(hoje.month, hoje.day) < (data_inicio.month, data_inicio.day):
            idade -= 1
        return idade
