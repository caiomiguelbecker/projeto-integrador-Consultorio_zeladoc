import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

from app.core.idioma import Idioma


class Prontuario_View:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self._pacientes = []
        self.configurar_janela()
        self.criar_componentes()
        self.configurar_treeview()
        self.configurar_eventos()

    def configurar_janela(self):
        self.root.title(Idioma.t("prontuario.janela_titulo"))
        self.root.geometry("700x600")
        self.root.resizable(False, False)

    def criar_componentes(self):
        self.lbl_titulo = ttk.Label(
            self.root,
            text=Idioma.t("prontuario.titulo"),
            font=("Arial", 16, "bold")
        )
        self.lbl_titulo.pack(pady=10)

        self.frm_dados = ttk.Labelframe(
            self.root,
            text=Idioma.t("prontuario.dados_frame"),
            padding=10
        )
        self.frm_dados.pack(fill=X, padx=15, pady=5)
        self.frm_dados.grid_columnconfigure(1, weight=1)

        self.lbl_id = ttk.Label(self.frm_dados, text=f"{Idioma.t('comum.id')}:")
        self.lbl_id.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        self.txt_id = ttk.Entry(self.frm_dados, width=10, state="readonly")
        self.txt_id.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        self.lbl_paciente = ttk.Label(self.frm_dados, text=f"{Idioma.t('prontuario.paciente')}:")
        self.lbl_paciente.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        self.cmb_paciente = ttk.Combobox(self.frm_dados, width=40, state="readonly")
        self.cmb_paciente.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        self.lbl_observacoes = ttk.Label(self.frm_dados, text=f"{Idioma.t('prontuario.observacoes')}:")
        self.lbl_observacoes.grid(row=2, column=0, padx=5, pady=5, sticky=NW)
        self.txt_observacoes = ttk.Text(self.frm_dados, width=48, height=6)
        self.txt_observacoes.grid(row=2, column=1, padx=5, pady=5, sticky=W)

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

        self.tbl_prontuarios = ttk.Treeview(self.root, height=8, bootstyle=PRIMARY)
        self.tbl_prontuarios.pack(fill=BOTH, expand=True, padx=15, pady=10)

    def configurar_treeview(self):
        self.tbl_prontuarios["columns"] = ("id", "paciente", "observacoes")
        self.tbl_prontuarios.column("#0", width=0, stretch=False)
        self.tbl_prontuarios.column("id", width=50, anchor="center")
        self.tbl_prontuarios.column("paciente", width=200)
        self.tbl_prontuarios.column("observacoes", width=350)
        self.tbl_prontuarios.heading("id", text=Idioma.t("comum.id"))
        self.tbl_prontuarios.heading("paciente", text=Idioma.t("prontuario.paciente"))
        self.tbl_prontuarios.heading("observacoes", text=Idioma.t("prontuario.observacoes"))

    def configurar_eventos(self):
        self.btn_novo.config(command=self.controller.new)
        self.btn_salvar.config(command=self.controller.save)
        self.btn_alterar.config(command=self.controller.update)
        self.btn_excluir.config(command=self.controller.delete)
        self.btn_fechar.config(command=self.fechar)
        self.tbl_prontuarios.bind("<<TreeviewSelect>>", self.controller.selecionar_prontuario)

    def carregar_pacientes(self, pacientes):
        self._pacientes = pacientes
        valores = [f"{p.id} - {p.nome}" for p in pacientes]
        self.cmb_paciente["values"] = valores
        self.cmb_paciente.set("")

    def preencher_campos(self, prontuario):
        self.limpar_campos()
        self.txt_id.config(state="normal")
        self.txt_id.insert(0, str(prontuario.id))
        self.txt_id.config(state="readonly")
        self.txt_observacoes.insert("1.0", prontuario.observacoes)

        for indice, paciente in enumerate(self._pacientes):
            if paciente.id == prontuario.paciente.id:
                self.cmb_paciente.current(indice)
                break

    def limpar_campos(self):
        self.txt_id.config(state="normal")
        self.txt_id.delete(0, "end")
        self.txt_id.config(state="readonly")
        self.txt_observacoes.delete("1.0", "end")
        self.cmb_paciente.set("")
        self.cmb_paciente.focus()

    def limpar_treeview(self):
        for item in self.tbl_prontuarios.get_children():
            self.tbl_prontuarios.delete(item)

    def get_id_selecionado(self):
        item = self.tbl_prontuarios.selection()[0]
        return self.tbl_prontuarios.item(item)["values"][0]

    def confirmar_exclusao(self):
        return messagebox.askyesno(
            Idioma.t("comum.confirmacao"),
            Idioma.t("prontuario.confirmar_exclusao"),
            parent=self.root
        )

    def ler_dados_prontuario(self):
        observacoes = self.txt_observacoes.get("1.0", "end").strip()

        indice_paciente = self.cmb_paciente.current()
        if indice_paciente < 0:
            raise ValueError("prontuario.erro_paciente_nao_selecionado")
        paciente = self._pacientes[indice_paciente]

        return observacoes, paciente

    def exibir_mensagem(self, mensagem, sucesso=True):
        if sucesso:
            messagebox.showinfo(Idioma.t("app_titulo"), mensagem, parent=self.root)
        else:
            messagebox.showerror(Idioma.t("app_titulo"), mensagem, parent=self.root)

    def exibir_prontuarios(self, prontuarios):
        self.limpar_treeview()
        for prontuario in prontuarios:
            resumo = prontuario.observacoes
            if len(resumo) > 60:
                resumo = resumo[:57] + "..."
            self.tbl_prontuarios.insert(
                "", "end",
                values=(prontuario.id, prontuario.paciente.nome, resumo)
            )

    def fechar(self):
        self.root.destroy()

    def iniciar(self):
        self.controller.carregar_pacientes()
        self.controller.get_all()