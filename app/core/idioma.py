idioma_atual = "pt"

textos = {
    "app_titulo": {"pt": "ZELADOC", "en": "ZELADOC"},
    "menu_pacientes": {"pt": "Pacientes", "en": "Patients"},
    "menu_medicos": {"pt": "Médicos", "en": "Doctors"},
    "menu_consultas": {"pt": "Consultas", "en": "Appointments"},
    "menu_usuarios": {"pt": "Usuários", "en": "Users"},
    "menu_convenios": {"pt": "Convênios", "en": "Insurance Plans"},
    "menu_especialidades": {"pt": "Especialidades", "en": "Specialties"},
    "menu_exames": {"pt": "Exames", "en": "Exams"},
    "menu_prontuarios": {"pt": "Prontuários", "en": "Medical Records"},
    "menu_sair": {"pt": "Sair", "en": "Exit"},
    "menu_idioma": {"pt": "English", "en": "Português"},

    "nome": {"pt": "Nome:", "en": "Name:"},
    "data_nascimento": {"pt": "Data de nascimento (AAAA-MM-DD):", "en": "Date of birth (YYYY-MM-DD):"},
    "convenio_campo": {"pt": "Convênio:", "en": "Insurance Plan:"},
    "logradouro": {"pt": "Logradouro:", "en": "Street:"},
    "numero": {"pt": "Número:", "en": "Number:"},
    "cidade": {"pt": "Cidade:", "en": "City:"},
    "uf": {"pt": "UF:", "en": "State:"},
    "cadastro_paciente": {"pt": "Cadastro de Paciente", "en": "Patient Registration"},

    "crm": {"pt": "CRM:", "en": "License:"},
    "especialidade_campo": {"pt": "Especialidade:", "en": "Specialty:"},
    "usuario_login": {"pt": "Usuário (login):", "en": "User (login):"},
    "cadastro_medico": {"pt": "Cadastro de Médico", "en": "Doctor Registration"},

    "paciente_campo": {"pt": "Paciente:", "en": "Patient:"},
    "medico_campo": {"pt": "Médico:", "en": "Doctor:"},
    "data_hora": {"pt": "Data e hora (AAAA-MM-DD HH:MM):", "en": "Date and time (YYYY-MM-DD HH:MM):"},
    "agendar_consulta": {"pt": "Agendar Consulta", "en": "Schedule Appointment"},

    "email": {"pt": "Email:", "en": "Email:"},
    "senha": {"pt": "Senha:", "en": "Password:"},
    "cadastro_usuario": {"pt": "Cadastro de Usuário", "en": "User Registration"},

    "cadastro_convenio": {"pt": "Cadastro de Convênio", "en": "Insurance Plan Registration"},
    "cadastro_especialidade": {"pt": "Cadastro de Especialidade", "en": "Specialty Registration"},
    "cadastro_exame": {"pt": "Cadastro de Exame", "en": "Exam Registration"},

    "observacoes": {"pt": "Observações:", "en": "Notes:"},
    "cadastro_prontuario": {"pt": "Cadastro de Prontuário", "en": "Medical Record Registration"},

    "botao_salvar": {"pt": "Salvar", "en": "Save"},
}

def t(chave):
    return textos[chave][idioma_atual]

def trocar_idioma():
    global idioma_atual
    idioma_atual = "en" if idioma_atual == "pt" else "pt"