import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

from app.core.idioma import Idioma


class Medico_View:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self._especialidades = []
        self._usuarios = []
        self.configurar_janela()
        self.criar_componentes()
        self.configurar_treeview()
        self.configurar_eventos()

    def configurar_janela(self):
        self.root.title(Idioma.t("medico.janela_titulo"))
        self.root.geometry("680x560")
        self.root.resizable(False, False)

    def criar_componentes(self):
        self.lbl_titulo = ttk.Label(
            self.root,
            text=Idioma.t("medico.titulo"),
            font=("Arial", 16, "bold")
        )
        self.lbl_titulo.pack(pady=10)

        self.frm_dados = ttk.Labelframe(
            self.root,
            text=Idioma.t("medico.dados_frame"),
            padding=10
        )
        self.frm_dados.pack(fill=X, padx=15, pady=5)
        self.frm_dados.grid_columnconfigure(1, weight=1)
        self.frm_dados.grid_columnconfigure(3, weight=1)

        self.lbl_id = ttk.Label(self.frm_dados, text=f"{Idioma.t('comum.id')}:")
        self.lbl_id.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        self.txt_id = ttk.Entry(self.frm_dados, width=10, state="readonly")
        self.txt_id.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        self.lbl_crm = ttk.Label(self.frm_dados, text=f"{Idioma.t('medico.crm')}:")
        self.lbl_crm.grid(row=0, column=2, padx=5, pady=5, sticky=W)
        self.txt_crm = ttk.Entry(self.frm_dados, width=20)
        self.txt_crm.grid(row=0, column=3, padx=5, pady=5, sticky=W)

        self.lbl_nome = ttk.Label(self.frm_dados, text=f"{Idioma.t('comum.nome')}:")
        self.lbl_nome.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        self.txt_nome = ttk.Entry(self.frm_dados, width=40)
        self.txt_nome.grid(row=1, column=1, padx=5, pady=5, columnspan=3, sticky=W)

        self.lbl_especialidade = ttk.Label(self.frm_dados, text=f"{Idioma.t('medico.especialidade')}:")
        self.lbl_especialidade.grid(row=2, column=0, padx=5, pady=5, sticky=W)
        self.cmb_especialidade = ttk.Combobox(self.frm_dados, width=37, state="readonly")
        self.cmb_especialidade.grid(row=2, column=1, padx=5, pady=5, columnspan=3, sticky=W)

        self.lbl_usuario = ttk.Label(self.frm_dados, text=f"{Idioma.t('medico.usuario')}:")
        self.lbl_usuario.grid(row=3, column=0, padx=5, pady=5, sticky=W)
        self.cmb_usuario = ttk.Combobox(self.frm_dados, width=37, state="readonly")
        self.cmb_usuario.grid(row=3, column=1, padx=5, pady=5, columnspan=3, sticky=W)

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

        self.tbl_medicos = ttk.Treeview(self.root, height=10, bootstyle=PRIMARY)
        self.tbl_medicos.pack(fill=BOTH, expand=True, padx=15, pady=10)

    def configurar_treeview(self):
        self.tbl_medicos["columns"] = ("id", "nome", "crm", "especialidade", "usuario")
        self.tbl_medicos.column("#0", width=0, stretch=False)
        self.tbl_medicos.column("id", width=50, anchor="center")
        self.tbl_medicos.column("nome", width=170)
        self.tbl_medicos.column("crm", width=90, anchor="center")
        self.tbl_medicos.column("especialidade", width=150)
        self.tbl_medicos.column("usuario", width=150)
        self.tbl_medicos.heading("id", text=Idioma.t("comum.id"))
        self.tbl_medicos.heading("nome", text=Idioma.t("comum.nome"))
        self.tbl_medicos.heading("crm", text=Idioma.t("medico.crm"))
        self.tbl_medicos.heading("especialidade", text=Idioma.t("medico.especialidade"))
        self.tbl_medicos.heading("usuario", text=Idioma.t("medico.usuario"))

    def configurar_eventos(self):
        self.btn_novo.config(command=self.controller.new)
        self.btn_salvar.config(command=self.controller.save)
        self.btn_alterar.config(command=self.controller.update)
        self.btn_excluir.config(command=self.controller.delete)
        self.btn_fechar.config(command=self.fechar)
        self.tbl_medicos.bind("<<TreeviewSelect>>", self.controller.selecionar_medico)

    def carregar_especialidades(self, especialidades):
        self._especialidades = especialidades
        valores = [f"{e.id} - {e.nome}" for e in especialidades]
        self.cmb_especialidade["values"] = valores
        self.cmb_especialidade.set("")

    def carregar_usuarios(self, usuarios):
        self._usuarios = usuarios
        valores = [f"{u.id} - {u.nome}" for u in usuarios]
        self.cmb_usuario["values"] = valores
        self.cmb_usuario.set("")

    def preencher_campos(self, medico):
        self.limpar_campos()
        self.txt_id.config(state="normal")
        self.txt_id.insert(0, str(medico.id))
        self.txt_id.config(state="readonly")
        self.txt_nome.insert(0, medico.nome)
        self.txt_crm.insert(0, medico.crm)

        for indice, especialidade in enumerate(self._especialidades):
            if especialidade.id == medico.especialidade.id:
                self.cmb_especialidade.current(indice)
                break

        for indice, usuario in enumerate(self._usuarios):
            if usuario.id == medico.usuario.id:
                self.cmb_usuario.current(indice)
                break

    def limpar_campos(self):
        self.txt_id.config(state="normal")
        self.txt_id.delete(0, "end")
        self.txt_id.config(state="readonly")
        self.txt_nome.delete(0, "end")
        self.txt_crm.delete(0, "end")
        self.cmb_especialidade.set("")
        self.cmb_usuario.set("")
        self.txt_nome.focus()

    def limpar_treeview(self):
        for item in self.tbl_medicos.get_children():
            self.tbl_medicos.delete(item)

    def get_id_selecionado(self):
        item = self.tbl_medicos.selection()[0]
        return self.tbl_medicos.item(item)["values"][0]

    def confirmar_exclusao(self):
        return messagebox.askyesno(
            Idioma.t("comum.confirmacao"),
            Idioma.t("medico.confirmar_exclusao"),
            parent=self.root
        )

    def ler_dados_medico(self):
        nome = self.txt_nome.get()
        crm = self.txt_crm.get()

        indice_especialidade = self.cmb_especialidade.current()
        if indice_especialidade < 0:
            raise ValueError("medico.erro_especialidade_nao_selecionada")
        especialidade = self._especialidades[indice_especialidade]

        indice_usuario = self.cmb_usuario.current()
        if indice_usuario < 0:
            raise ValueError("medico.erro_usuario_nao_selecionado")
        usuario = self._usuarios[indice_usuario]

        return nome, crm, especialidade, usuario

    def exibir_mensagem(self, mensagem, sucesso=True):
        if sucesso:
            messagebox.showinfo(Idioma.t("app_titulo"), mensagem, parent=self.root)
        else:
            messagebox.showerror(Idioma.t("app_titulo"), mensagem, parent=self.root)

    def exibir_medicos(self, medicos):
        self.limpar_treeview()
        for medico in medicos:
            self.tbl_medicos.insert(
                "", "end",
                values=(
                    medico.id,
                    medico.nome,
                    medico.crm,
                    medico.especialidade.nome,
                    medico.usuario.nome
                )
            )

    def fechar(self):
        self.root.destroy()

    def iniciar(self):
        self.controller.carregar_especialidades()
        self.controller.carregar_usuarios()
        self.controller.get_all()