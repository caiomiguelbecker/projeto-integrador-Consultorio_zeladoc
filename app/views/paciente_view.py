import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

from app.core.idioma import Idioma
from app.core.data_utils import Data_Utils


class Paciente_View:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self._convenios = []
        self.configurar_janela()
        self.criar_componentes()
        self.configurar_treeview()
        self.configurar_eventos()

    def configurar_janela(self):
        self.root.title(Idioma.t("paciente.janela_titulo"))
        self.root.geometry("760x680")
        self.root.resizable(False, False)

    def criar_componentes(self):
        self.lbl_titulo = ttk.Label(
            self.root,
            text=Idioma.t("paciente.titulo"),
            font=("Arial", 16, "bold")
        )
        self.lbl_titulo.pack(pady=10)

        # ------- Dados do paciente -------
        self.frm_dados = ttk.Labelframe(
            self.root,
            text=Idioma.t("paciente.dados_frame"),
            padding=10
        )
        self.frm_dados.pack(fill=X, padx=15, pady=5)
        self.frm_dados.grid_columnconfigure(1, weight=1)
        self.frm_dados.grid_columnconfigure(3, weight=1)

        self.lbl_id = ttk.Label(self.frm_dados, text=f"{Idioma.t('comum.id')}:")
        self.lbl_id.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        self.txt_id = ttk.Entry(self.frm_dados, width=10, state="readonly")
        self.txt_id.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        self.lbl_idade = ttk.Label(self.frm_dados, text=f"{Idioma.t('paciente.idade')}:")
        self.lbl_idade.grid(row=0, column=2, padx=5, pady=5, sticky=W)
        self.txt_idade = ttk.Entry(self.frm_dados, width=10, state="readonly")
        self.txt_idade.grid(row=0, column=3, padx=5, pady=5, sticky=W)

        self.lbl_nome = ttk.Label(self.frm_dados, text=f"{Idioma.t('comum.nome')}:")
        self.lbl_nome.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        self.txt_nome = ttk.Entry(self.frm_dados, width=40)
        self.txt_nome.grid(row=1, column=1, padx=5, pady=5, columnspan=3, sticky=W)

        self.lbl_data_nascimento = ttk.Label(self.frm_dados, text=f"{Idioma.t('paciente.nascimento')}:")
        self.lbl_data_nascimento.grid(row=2, column=0, padx=5, pady=5, sticky=W)
        self.txt_data_nascimento = ttk.Entry(self.frm_dados, width=20)
        self.txt_data_nascimento.grid(row=2, column=1, padx=5, pady=5, sticky=W)

        self.lbl_convenio = ttk.Label(self.frm_dados, text=f"{Idioma.t('paciente.convenio')}:")
        self.lbl_convenio.grid(row=2, column=2, padx=5, pady=5, sticky=W)
        self.cmb_convenio = ttk.Combobox(self.frm_dados, width=25, state="readonly")
        self.cmb_convenio.grid(row=2, column=3, padx=5, pady=5, sticky=W)

        # ------- Endereço -------
        self.frm_endereco = ttk.Labelframe(
            self.root,
            text=Idioma.t("paciente.dados_endereco_frame"),
            padding=10
        )
        self.frm_endereco.pack(fill=X, padx=15, pady=5)
        self.frm_endereco.grid_columnconfigure(1, weight=1)
        self.frm_endereco.grid_columnconfigure(3, weight=1)

        self.lbl_logradouro = ttk.Label(self.frm_endereco, text=f"{Idioma.t('paciente.logradouro')}:")
        self.lbl_logradouro.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        self.txt_logradouro = ttk.Entry(self.frm_endereco, width=40)
        self.txt_logradouro.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        self.lbl_numero = ttk.Label(self.frm_endereco, text=f"{Idioma.t('paciente.numero')}:")
        self.lbl_numero.grid(row=0, column=2, padx=5, pady=5, sticky=W)
        self.txt_numero = ttk.Entry(self.frm_endereco, width=10)
        self.txt_numero.grid(row=0, column=3, padx=5, pady=5, sticky=W)

        self.lbl_cidade = ttk.Label(self.frm_endereco, text=f"{Idioma.t('paciente.cidade')}:")
        self.lbl_cidade.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        self.txt_cidade = ttk.Entry(self.frm_endereco, width=30)
        self.txt_cidade.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        self.lbl_uf = ttk.Label(self.frm_endereco, text=f"{Idioma.t('paciente.uf')}:")
        self.lbl_uf.grid(row=1, column=2, padx=5, pady=5, sticky=W)
        self.txt_uf = ttk.Entry(self.frm_endereco, width=6)
        self.txt_uf.grid(row=1, column=3, padx=5, pady=5, sticky=W)

        # ------- Botões -------
        self.frm_botoes = ttk.Frame(self.root)
        self.frm_botoes.pack(pady=10)

        self.btn_novo = ttk.Button(self.frm_botoes, text=Idioma.t("comum.novo"), bootstyle=PRIMARY, width=12)
        self.btn_novo.grid(row=0, column=0, padx=4)

        self.btn_salvar = ttk.Button(self.frm_botoes, text=Idioma.t("comum.salvar"), bootstyle=SUCCESS, width=12)
        self.btn_salvar.grid(row=0, column=1, padx=4)

        self.btn_alterar = ttk.Button(self.frm_botoes, text=Idioma.t("comum.alterar"), bootstyle=INFO, width=12)
        self.btn_alterar.grid(row=0, column=2, padx=4)

        self.btn_excluir = ttk.Button(self.frm_botoes, text=Idioma.t("comum.excluir"), bootstyle=DANGER, width=12)
        self.btn_excluir.grid(row=0, column=3, padx=4)

        self.btn_fechar = ttk.Button(self.frm_botoes, text=Idioma.t("comum.fechar"), bootstyle=SECONDARY, width=12)
        self.btn_fechar.grid(row=0, column=4, padx=4)

        self.tbl_pacientes = ttk.Treeview(self.root, height=10, bootstyle=PRIMARY)
        self.tbl_pacientes.pack(fill=BOTH, expand=True, padx=15, pady=10)

    def configurar_treeview(self):
        self.tbl_pacientes["columns"] = ("id", "nome", "nascimento", "idade", "convenio", "cidade", "uf")
        self.tbl_pacientes.column("#0", width=0, stretch=False)
        self.tbl_pacientes.column("id", width=45, anchor="center")
        self.tbl_pacientes.column("nome", width=170)
        self.tbl_pacientes.column("nascimento", width=90, anchor="center")
        self.tbl_pacientes.column("idade", width=55, anchor="center")
        self.tbl_pacientes.column("convenio", width=110)
        self.tbl_pacientes.column("cidade", width=110)
        self.tbl_pacientes.column("uf", width=45, anchor="center")
        self.tbl_pacientes.heading("id", text=Idioma.t("comum.id"))
        self.tbl_pacientes.heading("nome", text=Idioma.t("comum.nome"))
        self.tbl_pacientes.heading("nascimento", text=Idioma.t("paciente.nascimento"))
        self.tbl_pacientes.heading("idade", text=Idioma.t("paciente.idade"))
        self.tbl_pacientes.heading("convenio", text=Idioma.t("paciente.convenio"))
        self.tbl_pacientes.heading("cidade", text=Idioma.t("paciente.cidade"))
        self.tbl_pacientes.heading("uf", text=Idioma.t("paciente.uf"))

    def configurar_eventos(self):
        self.btn_novo.config(command=self.controller.new)
        self.btn_salvar.config(command=self.controller.save)
        self.btn_alterar.config(command=self.controller.update)
        self.btn_excluir.config(command=self.controller.delete)
        self.btn_fechar.config(command=self.fechar)
        self.tbl_pacientes.bind("<<TreeviewSelect>>", self.controller.selecionar_paciente)

    def carregar_convenios(self, convenios):
        self._convenios = convenios
        valores = [f"{c.id} - {c.nome}" for c in convenios]
        self.cmb_convenio["values"] = valores
        self.cmb_convenio.set("")

    def preencher_campos(self, paciente):
        self.limpar_campos()
        self.txt_id.config(state="normal")
        self.txt_id.insert(0, str(paciente.id))
        self.txt_id.config(state="readonly")

        self.txt_nome.insert(0, paciente.nome)
        self.txt_data_nascimento.insert(0, Data_Utils.data_para_string(paciente.data_nascimento))

        self.txt_idade.config(state="normal")
        self.txt_idade.insert(0, str(paciente.idade))
        self.txt_idade.config(state="readonly")

        if paciente.convenio is not None:
            for indice, convenio in enumerate(self._convenios):
                if convenio.id == paciente.convenio.id:
                    self.cmb_convenio.current(indice)
                    break

        if paciente.endereco is not None:
            self.txt_logradouro.insert(0, paciente.endereco.logradouro)
            self.txt_numero.insert(0, str(paciente.endereco.numero))
            self.txt_cidade.insert(0, paciente.endereco.cidade)
            self.txt_uf.insert(0, paciente.endereco.uf)

    def limpar_campos(self):
        self.txt_id.config(state="normal")
        self.txt_id.delete(0, "end")
        self.txt_id.config(state="readonly")
        self.txt_nome.delete(0, "end")
        self.txt_data_nascimento.delete(0, "end")
        self.txt_idade.config(state="normal")
        self.txt_idade.delete(0, "end")
        self.txt_idade.config(state="readonly")
        self.cmb_convenio.set("")
        self.txt_logradouro.delete(0, "end")
        self.txt_numero.delete(0, "end")
        self.txt_cidade.delete(0, "end")
        self.txt_uf.delete(0, "end")
        self.txt_nome.focus()

    def limpar_treeview(self):
        for item in self.tbl_pacientes.get_children():
            self.tbl_pacientes.delete(item)

    def get_id_selecionado(self):
        item = self.tbl_pacientes.selection()[0]
        return self.tbl_pacientes.item(item)["values"][0]

    def confirmar_exclusao(self):
        return messagebox.askyesno(
            Idioma.t("comum.confirmacao"),
            Idioma.t("paciente.confirmar_exclusao"),
            parent=self.root
        )

    def ler_dados_paciente(self):
        nome = self.txt_nome.get()
        data_nascimento = self.txt_data_nascimento.get()

        indice_convenio = self.cmb_convenio.current()
        convenio = self._convenios[indice_convenio] if indice_convenio >= 0 else None

        logradouro = self.txt_logradouro.get()
        numero = self.txt_numero.get()
        cidade = self.txt_cidade.get()
        uf = self.txt_uf.get()

        return nome, data_nascimento, convenio, logradouro, numero, cidade, uf

    def exibir_mensagem(self, mensagem, sucesso=True):
        if sucesso:
            messagebox.showinfo(Idioma.t("app_titulo"), mensagem, parent=self.root)
        else:
            messagebox.showerror(Idioma.t("app_titulo"), mensagem, parent=self.root)

    def exibir_pacientes(self, pacientes):
        self.limpar_treeview()
        for paciente in pacientes:
            nome_convenio = paciente.convenio.nome if paciente.convenio else "-"
            cidade = paciente.endereco.cidade if paciente.endereco else "-"
            uf = paciente.endereco.uf if paciente.endereco else "-"
            self.tbl_pacientes.insert(
                "", "end",
                values=(
                    paciente.id,
                    paciente.nome,
                    Data_Utils.data_para_string(paciente.data_nascimento),
                    paciente.idade,
                    nome_convenio,
                    cidade,
                    uf
                )
            )

    def fechar(self):
        self.root.destroy()

    def iniciar(self):
        self.controller.carregar_convenios()
        self.controller.get_all()