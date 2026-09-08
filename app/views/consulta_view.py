import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from app.core.idioma import t

class Consulta_View:
    def __init__(self, master):
        self.janela = ttk.Toplevel(master)
        self.janela.title(t("menu_consultas"))
        self.janela.geometry("350x350")

        ttk.Label(self.janela, text=t("agendar_consulta"), font=("Arial", 14, "bold")).pack(pady=10)

        ttk.Label(self.janela, text=t("paciente_campo")).pack(anchor=W, padx=20)
        self.campo_paciente = ttk.Entry(self.janela, width=30)
        self.campo_paciente.pack(padx=20, pady=5)

        ttk.Label(self.janela, text=t("medico_campo")).pack(anchor=W, padx=20)
        self.campo_medico = ttk.Entry(self.janela, width=30)
        self.campo_medico.pack(padx=20, pady=5)

        ttk.Label(self.janela, text=t("data_hora")).pack(anchor=W, padx=20)
        self.campo_data_hora = ttk.Entry(self.janela, width=30)
        self.campo_data_hora.pack(padx=20, pady=5)

        ttk.Button(self.janela, text=t("botao_salvar"), command=self.salvar, bootstyle=SUCCESS).pack(pady=15)

    def salvar(self):
        paciente = self.campo_paciente.get()
        medico = self.campo_medico.get()
        data_hora = self.campo_data_hora.get()
        print(f"[TODO: ligar ao controller] Salvar consulta: {paciente}, {medico}, {data_hora}")