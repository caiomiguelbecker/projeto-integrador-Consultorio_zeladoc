import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from app.core.idioma import t

class Paciente_View:
    def __init__(self, master):
        self.janela = ttk.Toplevel(master)
        self.janela.title(t("menu_pacientes"))
        self.janela.geometry("350x620")

        ttk.Label(self.janela, text=t("cadastro_paciente"), font=("Arial", 14, "bold")).pack(pady=10)

        ttk.Label(self.janela, text=t("nome")).pack(anchor=W, padx=20)
        self.campo_nome = ttk.Entry(self.janela, width=30)
        self.campo_nome.pack(padx=20, pady=5)

        ttk.Label(self.janela, text=t("data_nascimento")).pack(anchor=W, padx=20)
        self.campo_data = ttk.Entry(self.janela, width=30)
        self.campo_data.pack(padx=20, pady=5)

        ttk.Label(self.janela, text=t("convenio_campo")).pack(anchor=W, padx=20)
        self.campo_convenio = ttk.Entry(self.janela, width=30)
        self.campo_convenio.pack(padx=20, pady=5)

        ttk.Label(self.janela, text=t("logradouro")).pack(anchor=W, padx=20)
        self.campo_logradouro = ttk.Entry(self.janela, width=30)
        self.campo_logradouro.pack(padx=20, pady=5)

        ttk.Label(self.janela, text=t("numero")).pack(anchor=W, padx=20)
        self.campo_numero = ttk.Entry(self.janela, width=30)
        self.campo_numero.pack(padx=20, pady=5)

        ttk.Label(self.janela, text=t("cidade")).pack(anchor=W, padx=20)
        self.campo_cidade = ttk.Entry(self.janela, width=30)
        self.campo_cidade.pack(padx=20, pady=5)

        ttk.Label(self.janela, text=t("uf")).pack(anchor=W, padx=20)
        self.campo_uf = ttk.Entry(self.janela, width=30)
        self.campo_uf.pack(padx=20, pady=5)

        ttk.Button(self.janela, text=t("botao_salvar"), command=self.salvar, bootstyle=SUCCESS).pack(pady=15)

    def salvar(self):
        nome = self.campo_nome.get()
        data = self.campo_data.get()
        convenio = self.campo_convenio.get()
        logradouro = self.campo_logradouro.get()
        numero = self.campo_numero.get()
        cidade = self.campo_cidade.get()
        uf = self.campo_uf.get()
        print(f"[TODO: ligar ao controller] Salvar paciente: {nome}, {data}, convênio: {convenio}, endereço: {logradouro}, {numero}, {cidade}/{uf}")