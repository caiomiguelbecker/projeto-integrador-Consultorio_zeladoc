import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

from app.core.idioma import Idioma


class Convenio_View:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.configurar_janela()
        self.criar_componentes()
        self.configurar_treeview()
        self.configurar_eventos()

    def configurar_janela(self):
        self.root.title(Idioma.t("convenio.janela_titulo"))
        self.root.geometry("560x460")
        self.root.resizable(False, False)

    def criar_componentes(self):
        self.lbl_titulo = ttk.Label(
            self.root,
            text=Idioma.t("convenio.titulo"),
            font=("Arial", 16, "bold")
        )
        self.lbl_titulo.pack(pady=10)

        self.frm_dados = ttk.Labelframe(
            self.root,
            text=Idioma.t("convenio.dados_frame"),
            padding=10
        )
        self.frm_dados.pack(fill=X, padx=15, pady=5)
        self.frm_dados.grid_columnconfigure(1, weight=1)

        self.lbl_id = ttk.Label(self.frm_dados, text=f"{Idioma.t('comum.id')}:")
        self.lbl_id.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        self.txt_id = ttk.Entry(self.frm_dados, width=10, state="readonly")
        self.txt_id.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        self.lbl_nome = ttk.Label(self.frm_dados, text=f"{Idioma.t('comum.nome')}:")
        self.lbl_nome.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        self.txt_nome = ttk.Entry(self.frm_dados, width=40)
        self.txt_nome.grid(row=1, column=1, padx=5, pady=5, sticky=W)

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

        self.tbl_convenios = ttk.Treeview(self.root, height=10, bootstyle=PRIMARY)
        self.tbl_convenios.pack(fill=BOTH, expand=True, padx=15, pady=10)

    def configurar_treeview(self):
        self.tbl_convenios["columns"] = ("id", "nome")
        self.tbl_convenios.column("#0", width=0, stretch=False)
        self.tbl_convenios.column("id", width=60, anchor="center")
        self.tbl_convenios.column("nome", width=300)
        self.tbl_convenios.heading("id", text=Idioma.t("comum.id"))
        self.tbl_convenios.heading("nome", text=Idioma.t("comum.nome"))

    def configurar_eventos(self):
        self.btn_novo.config(command=self.controller.new)
        self.btn_salvar.config(command=self.controller.save)
        self.btn_alterar.config(command=self.controller.update)
        self.btn_excluir.config(command=self.controller.delete)
        self.btn_fechar.config(command=self.fechar)
        self.tbl_convenios.bind("<<TreeviewSelect>>", self.controller.selecionar_convenio)

    def preencher_campos(self, convenio):
        self.limpar_campos()
        self.txt_id.config(state="normal")
        self.txt_id.insert(0, str(convenio.id))
        self.txt_id.config(state="readonly")
        self.txt_nome.insert(0, convenio.nome)

    def limpar_campos(self):
        self.txt_id.config(state="normal")
        self.txt_id.delete(0, "end")
        self.txt_id.config(state="readonly")
        self.txt_nome.delete(0, "end")
        self.txt_nome.focus()

    def limpar_treeview(self):
        for item in self.tbl_convenios.get_children():
            self.tbl_convenios.delete(item)

    def get_id_selecionado(self):
        item = self.tbl_convenios.selection()[0]
        return self.tbl_convenios.item(item)["values"][0]

    def confirmar_exclusao(self):
        return messagebox.askyesno(
            Idioma.t("comum.confirmacao"),
            Idioma.t("convenio.confirmar_exclusao"),
            parent=self.root
        )

    def ler_dados_convenio(self):
        return self.txt_nome.get()

    def exibir_mensagem(self, mensagem, sucesso=True):
        if sucesso:
            messagebox.showinfo(Idioma.t("app_titulo"), mensagem, parent=self.root)
        else:
            messagebox.showerror(Idioma.t("app_titulo"), mensagem, parent=self.root)

    def exibir_convenios(self, convenios):
        self.limpar_treeview()
        for convenio in convenios:
            self.tbl_convenios.insert("", "end", values=(convenio.id, convenio.nome))

    def fechar(self):
        self.root.destroy()

    def iniciar(self):
        self.controller.get_all()