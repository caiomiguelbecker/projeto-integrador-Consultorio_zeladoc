import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

from app.core.idioma import Idioma
from app.core.data_utils import Data_Utils
from app.models.exame import Exame


class Consulta_View:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self._pacientes = []
        self._medicos = []
        self._exames = []
        self.configurar_janela()
        self.criar_componentes()
        self.configurar_treeview()
        self.configurar_eventos()

    def configurar_janela(self):
        self.root.title(Idioma.t("consulta.janela_titulo"))
        self.root.geometry("720x760")
        self.root.resizable(False, False)

    def criar_componentes(self):
        self.lbl_titulo = ttk.Label(
            self.root,
            text=Idioma.t("consulta.titulo"),
            font=("Arial", 16, "bold")
        )
        self.lbl_titulo.pack(pady=10)

        self.frm_dados = ttk.Labelframe(
            self.root,
            text=Idioma.t("consulta.dados_frame"),
            padding=10
        )
        self.frm_dados.pack(fill=X, padx=15, pady=5)
        self.frm_dados.grid_columnconfigure(1, weight=1)
        self.frm_dados.grid_columnconfigure(3, weight=1)

        self.lbl_id = ttk.Label(self.frm_dados, text=f"{Idioma.t('comum.id')}:")
        self.lbl_id.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        self.txt_id = ttk.Entry(self.frm_dados, width=10, state="readonly")
        self.txt_id.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        self.lbl_data_hora = ttk.Label(self.frm_dados, text=f"{Idioma.t('consulta.data_hora')}:")
        self.lbl_data_hora.grid(row=0, column=2, padx=5, pady=5, sticky=W)
        self.txt_data_hora = ttk.Entry(self.frm_dados, width=25)
        self.txt_data_hora.grid(row=0, column=3, padx=5, pady=5, sticky=W)

        self.lbl_paciente = ttk.Label(self.frm_dados, text=f"{Idioma.t('consulta.paciente')}:")
        self.lbl_paciente.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        self.cmb_paciente = ttk.Combobox(self.frm_dados, width=37, state="readonly")
        self.cmb_paciente.grid(row=1, column=1, padx=5, pady=5, columnspan=3, sticky=W)

        self.lbl_medico = ttk.Label(self.frm_dados, text=f"{Idioma.t('consulta.medico')}:")
        self.lbl_medico.grid(row=2, column=0, padx=5, pady=5, sticky=W)
        self.cmb_medico = ttk.Combobox(self.frm_dados, width=37, state="readonly")
        self.cmb_medico.grid(row=2, column=1, padx=5, pady=5, columnspan=3, sticky=W)

        # --- Exames vinculados a esta consulta ---
        self.frm_exames = ttk.Labelframe(
            self.root,
            text=Idioma.t("consulta.exames_frame"),
            padding=10
        )
        self.frm_exames.pack(fill=X, padx=15, pady=5)
        self.frm_exames.grid_columnconfigure(0, weight=1)

        self.lbl_exame = ttk.Label(self.frm_exames, text=f"{Idioma.t('consulta.exame')}:")
        self.lbl_exame.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        self.cmb_exame = ttk.Combobox(self.frm_exames, width=30, state="readonly")
        self.cmb_exame.grid(row=1, column=0, padx=5, pady=5, sticky=(W, E))

        self.btn_adicionar_exame = ttk.Button(
            self.frm_exames,
            text=Idioma.t("consulta.adicionar_exame"),
            bootstyle=SUCCESS,
            width=16
        )
        self.btn_adicionar_exame.grid(row=1, column=1, padx=5, pady=5)

        self.btn_remover_exame = ttk.Button(
            self.frm_exames,
            text=Idioma.t("consulta.remover_exame"),
            bootstyle=DANGER,
            width=16
        )
        self.btn_remover_exame.grid(row=1, column=2, padx=5, pady=5)

        self.lst_exames = ttk.Treeview(
            self.frm_exames, height=4, bootstyle=INFO, show="tree", selectmode="browse"
        )
        self.lst_exames.grid(row=2, column=0, columnspan=3, padx=5, pady=(5, 0), sticky=(W, E))
        self.lst_exames.column("#0", width=650)

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

        self.tbl_consultas = ttk.Treeview(self.root, height=10, bootstyle=PRIMARY)
        self.tbl_consultas.pack(fill=BOTH, expand=True, padx=15, pady=10)

    def configurar_treeview(self):
        self.tbl_consultas["columns"] = ("id", "data_hora", "paciente", "medico")
        self.tbl_consultas.column("#0", width=0, stretch=False)
        self.tbl_consultas.column("id", width=50, anchor="center")
        self.tbl_consultas.column("data_hora", width=140, anchor="center")
        self.tbl_consultas.column("paciente", width=200)
        self.tbl_consultas.column("medico", width=200)
        self.tbl_consultas.heading("id", text=Idioma.t("comum.id"))
        self.tbl_consultas.heading("data_hora", text=Idioma.t("consulta.data_hora"))
        self.tbl_consultas.heading("paciente", text=Idioma.t("consulta.paciente"))
        self.tbl_consultas.heading("medico", text=Idioma.t("consulta.medico"))

    def configurar_eventos(self):
        self.btn_novo.config(command=self.controller.new)
        self.btn_salvar.config(command=self.controller.save)
        self.btn_alterar.config(command=self.controller.update)
        self.btn_excluir.config(command=self.controller.delete)
        self.btn_fechar.config(command=self.fechar)
        self.btn_adicionar_exame.config(command=self.controller.adicionar_exame)
        self.btn_remover_exame.config(command=self.controller.remover_exame)
        self.tbl_consultas.bind("<<TreeviewSelect>>", self.controller.selecionar_consulta)

    def carregar_pacientes(self, pacientes):
        self._pacientes = pacientes
        valores = [f"{p.id} - {p.nome}" for p in pacientes]
        self.cmb_paciente["values"] = valores
        self.cmb_paciente.set("")

    def carregar_medicos(self, medicos):
        self._medicos = medicos
        valores = [f"{m.id} - {m.nome}" for m in medicos]
        self.cmb_medico["values"] = valores
        self.cmb_medico.set("")

    def carregar_exames(self, exames):
        self._exames = exames
        valores = [f"{e.id} - {e.nome}" for e in exames]
        self.cmb_exame["values"] = valores
        self.cmb_exame.set("")

    def exibir_exames_consulta(self, exames):
        for item in self.lst_exames.get_children():
            self.lst_exames.delete(item)
        for exame in exames:
            self.lst_exames.insert("", "end", iid=str(exame.id), text=exame.nome)

    def get_exame_para_adicionar(self):
        indice = self.cmb_exame.current()
        if indice < 0:
            raise ValueError("consulta.erro_exame_nao_selecionado")
        return self._exames[indice]

    def get_exame_selecionado_para_remover(self):
        selecao = self.lst_exames.selection()
        if not selecao:
            raise ValueError("consulta.erro_exame_nao_selecionado_lista")
        id_exame = int(selecao[0])
        nome_exame = self.lst_exames.item(selecao[0])["text"]
        return Exame(id_exame, nome_exame)

    def preencher_campos(self, consulta):
        self.limpar_campos()
        self.txt_id.config(state="normal")
        self.txt_id.insert(0, str(consulta.id))
        self.txt_id.config(state="readonly")
        self.txt_data_hora.insert(0, Data_Utils.data_hora_para_string(consulta.data_hora))

        for indice, paciente in enumerate(self._pacientes):
            if paciente.id == consulta.paciente.id:
                self.cmb_paciente.current(indice)
                break

        for indice, medico in enumerate(self._medicos):
            if medico.id == consulta.medico.id:
                self.cmb_medico.current(indice)
                break

    def limpar_campos(self):
        self.txt_id.config(state="normal")
        self.txt_id.delete(0, "end")
        self.txt_id.config(state="readonly")
        self.txt_data_hora.delete(0, "end")
        self.cmb_paciente.set("")
        self.cmb_medico.set("")
        self.cmb_exame.set("")
        self.exibir_exames_consulta([])
        self.txt_data_hora.focus()

    def limpar_treeview(self):
        for item in self.tbl_consultas.get_children():
            self.tbl_consultas.delete(item)

    def get_id_selecionado(self):
        item = self.tbl_consultas.selection()[0]
        return self.tbl_consultas.item(item)["values"][0]

    def confirmar_exclusao(self):
        return messagebox.askyesno(
            Idioma.t("comum.confirmacao"),
            Idioma.t("consulta.confirmar_exclusao"),
            parent=self.root
        )

    def ler_dados_consulta(self):
        data_hora = self.txt_data_hora.get()

        indice_paciente = self.cmb_paciente.current()
        if indice_paciente < 0:
            raise ValueError("consulta.erro_paciente_nao_selecionado")
        paciente = self._pacientes[indice_paciente]

        indice_medico = self.cmb_medico.current()
        if indice_medico < 0:
            raise ValueError("consulta.erro_medico_nao_selecionado")
        medico = self._medicos[indice_medico]

        return data_hora, paciente, medico

    def exibir_mensagem(self, mensagem, sucesso=True):
        if sucesso:
            messagebox.showinfo(Idioma.t("app_titulo"), mensagem, parent=self.root)
        else:
            messagebox.showerror(Idioma.t("app_titulo"), mensagem, parent=self.root)

    def exibir_consultas(self, consultas):
        self.limpar_treeview()
        for consulta in consultas:
            self.tbl_consultas.insert(
                "", "end",
                values=(
                    consulta.id,
                    Data_Utils.data_hora_para_string(consulta.data_hora),
                    consulta.paciente.nome,
                    consulta.medico.nome
                )
            )

    def fechar(self):
        self.root.destroy()

    def iniciar(self):
        self.controller.carregar_pacientes()
        self.controller.carregar_medicos()
        self.controller.carregar_exames()
        self.controller.get_all()