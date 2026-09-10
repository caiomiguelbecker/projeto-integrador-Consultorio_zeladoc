import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

from app.core.idioma import Idioma


class Usuario_View:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.configurar_janela()
        self.criar_componentes()
        self.configurar_treeview()
        self.configurar_eventos()

    def configurar_janela(self):
        self.root.title(Idioma.t("usuario.janela_titulo"))
        self.root.geometry("600x520")
        self.root.resizable(False, False)

    def criar_componentes(self):
        self.lbl_titulo = ttk.Label(
            self.root,
            text=Idioma.t("usuario.titulo"),
            font=("Arial", 16, "bold")
        )
        self.lbl_titulo.pack(pady=10)

        self.frm_dados = ttk.Labelframe(
            self.root,
            text=Idioma.t("usuario.dados_frame"),
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

        self.lbl_email = ttk.Label(self.frm_dados, text=f"{Idioma.t('usuario.email')}:")
        self.lbl_email.grid(row=2, column=0, padx=5, pady=5, sticky=W)
        self.txt_email = ttk.Entry(self.frm_dados, width=40)
        self.txt_email.grid(row=2, column=1, padx=5, pady=5, sticky=W)

        self.lbl_senha = ttk.Label(self.frm_dados, text=f"{Idioma.t('usuario.senha')}:")
        self.lbl_senha.grid(row=3, column=0, padx=5, pady=5, sticky=W)
        self.txt_senha = ttk.Entry(self.frm_dados, width=40, show="*")
        self.txt_senha.grid(row=3, column=1, padx=5, pady=5, sticky=W)

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

        self.tbl_usuarios = ttk.Treeview(self.root, height=10, bootstyle=PRIMARY)
        self.tbl_usuarios.pack(fill=BOTH, expand=True, padx=15, pady=10)

    def configurar_treeview(self):
        self.tbl_usuarios["columns"] = ("id", "nome", "email")
        self.tbl_usuarios.column("#0", width=0, stretch=False)
        self.tbl_usuarios.column("id", width=60, anchor="center")
        self.tbl_usuarios.column("nome", width=250)
        self.tbl_usuarios.column("email", width=250)
        self.tbl_usuarios.heading("id", text=Idioma.t("comum.id"))
        self.tbl_usuarios.heading("nome", text=Idioma.t("comum.nome"))
        self.tbl_usuarios.heading("email", text=Idioma.t("usuario.email"))

    def configurar_eventos(self):
        self.btn_novo.config(command=self.controller.new)
        self.btn_salvar.config(command=self.controller.save)
        self.btn_alterar.config(command=self.controller.update)
        self.btn_excluir.config(command=self.controller.delete)
        self.btn_fechar.config(command=self.fechar)
        self.tbl_usuarios.bind("<<TreeviewSelect>>", self.controller.selecionar_usuario)

    def preencher_campos(self, usuario):
        self.limpar_campos()
        self.txt_id.config(state="normal")
        self.txt_id.insert(0, str(usuario.id))
        self.txt_id.config(state="readonly")
        self.txt_nome.insert(0, usuario.nome)
        self.txt_email.insert(0, usuario.email)

    def limpar_campos(self):
        self.txt_id.config(state="normal")
        self.txt_id.delete(0, "end")
        self.txt_id.config(state="readonly")
        self.txt_nome.delete(0, "end")
        self.txt_email.delete(0, "end")
        self.txt_senha.delete(0, "end")
        self.txt_nome.focus()

    def limpar_treeview(self):
        for item in self.tbl_usuarios.get_children():
            self.tbl_usuarios.delete(item)

    def get_id_selecionado(self):
        item = self.tbl_usuarios.selection()[0]
        return self.tbl_usuarios.item(item)["values"][0]

    def confirmar_exclusao(self):
        return messagebox.askyesno(
            Idioma.t("comum.confirmacao"),
            Idioma.t("usuario.confirmar_exclusao"),
            parent=self.root
        )

    def ler_dados_usuario(self):
        nome = self.txt_nome.get()
        email = self.txt_email.get()
        senha = self.txt_senha.get()
        return nome, email, senha

    def exibir_mensagem(self, mensagem, sucesso=True):
        if sucesso:
            messagebox.showinfo(Idioma.t("app_titulo"), mensagem, parent=self.root)
        else:
            messagebox.showerror(Idioma.t("app_titulo"), mensagem, parent=self.root)

    def exibir_usuarios(self, usuarios):
        self.limpar_treeview()
        for usuario in usuarios:
            self.tbl_usuarios.insert("", "end", values=(usuario.id, usuario.nome, usuario.email))

    def fechar(self):
        self.root.destroy()

    def iniciar(self):
        self.controller.get_all()