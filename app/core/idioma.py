class Idioma:

    ATUAL = "pt"

    TEXTOS = {
        "pt": {
            "app_titulo": "ZELADOC",
            "menu_pacientes": "Pacientes",
            "menu_medicos": "Médicos",
            "menu_consultas": "Consultas",
            "menu_usuarios": "Usuários",
            "menu_convenios": "Convênios",
            "menu_especialidades": "Especialidades",
            "menu_exames": "Exames",
            "menu_prontuarios": "Prontuários",
            "menu_sair": "Sair",
            "menu_idioma": "English",

            "nome": "Nome:",
            "data_nascimento": "Data de nascimento (AAAA-MM-DD):",
            "convenio_campo": "Convênio:",
            "logradouro": "Logradouro:",
            "numero": "Número:",
            "cidade": "Cidade:",
            "uf": "UF:",
            "cadastro_paciente": "Cadastro de Paciente",

            "crm": "CRM:",
            "especialidade_campo": "Especialidade:",
            "usuario_login": "Usuário (login):",
            "cadastro_medico": "Cadastro de Médico",

            "paciente_campo": "Paciente:",
            "medico_campo": "Médico:",
            "data_hora": "Data e hora (AAAA-MM-DD HH:MM):",
            "agendar_consulta": "Agendar Consulta",

            "email": "Email:",
            "senha": "Senha:",
            "cadastro_usuario": "Cadastro de Usuário",

            "cadastro_convenio": "Cadastro de Convênio",
            "cadastro_especialidade": "Cadastro de Especialidade",
            "cadastro_exame": "Cadastro de Exame",

            "observacoes": "Observações:",
            "cadastro_prontuario": "Cadastro de Prontuário",

            "botao_salvar": "Salvar",
        },
        "en": {
            "app_titulo": "ZELADOC",
            "menu_pacientes": "Patients",
            "menu_medicos": "Doctors",
            "menu_consultas": "Appointments",
            "menu_usuarios": "Users",
            "menu_convenios": "Insurance Plans",
            "menu_especialidades": "Specialties",
            "menu_exames": "Exams",
            "menu_prontuarios": "Medical Records",
            "menu_sair": "Exit",
            "menu_idioma": "Português",

            "nome": "Name:",
            "data_nascimento": "Date of birth (YYYY-MM-DD):",
            "convenio_campo": "Insurance Plan:",
            "logradouro": "Street:",
            "numero": "Number:",
            "cidade": "City:",
            "uf": "State:",
            "cadastro_paciente": "Patient Registration",

            "crm": "License:",
            "especialidade_campo": "Specialty:",
            "usuario_login": "User (login):",
            "cadastro_medico": "Doctor Registration",

            "paciente_campo": "Patient:",
            "medico_campo": "Doctor:",
            "data_hora": "Date and time (YYYY-MM-DD HH:MM):",
            "agendar_consulta": "Schedule Appointment",

            "email": "Email:",
            "senha": "Password:",
            "cadastro_usuario": "User Registration",

            "cadastro_convenio": "Insurance Plan Registration",
            "cadastro_especialidade": "Specialty Registration",
            "cadastro_exame": "Exam Registration",

            "observacoes": "Notes:",
            "cadastro_prontuario": "Medical Record Registration",

            "botao_salvar": "Save",
        }
    }

    @classmethod
    def definir(cls, codigo):
        cls.ATUAL = codigo

    @classmethod
    def t(cls, chave):
        return cls.TEXTOS[cls.ATUAL].get(chave, chave)


def t(chave):
    return Idioma.t(chave)


def trocar_idioma():
    Idioma.definir("en" if Idioma.ATUAL == "pt" else "pt")