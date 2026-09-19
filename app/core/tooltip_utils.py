import tkinter as tk


class Tooltip:
    
    def __init__(self, widget, texto, atraso_ms=400):
        self.widget = widget
        self.texto = texto
        self.atraso_ms = atraso_ms
        self._id_agendado = None
        self._janela = None

        widget.bind("<Enter>", self._ao_entrar, add="+")
        widget.bind("<Leave>", self._ao_sair, add="+")
        widget.bind("<ButtonPress>", self._ao_sair, add="+")

    def _ao_entrar(self, event=None):
        self._agendar()

    def _ao_sair(self, event=None):
        self._cancelar_agendamento()
        self._esconder()

    def _agendar(self):
        self._cancelar_agendamento()
        self._id_agendado = self.widget.after(self.atraso_ms, self._mostrar)

    def _cancelar_agendamento(self):
        if self._id_agendado is not None:
            self.widget.after_cancel(self._id_agendado)
            self._id_agendado = None

    def _mostrar(self):
        if self._janela is not None:
            return

        x = self.widget.winfo_rootx() + 20
        y = self.widget.winfo_rooty() + self.widget.winfo_height() + 8

        self._janela = tk.Toplevel(self.widget)
        self._janela.overrideredirect(True)
        self._janela.attributes("-topmost", True)
        self._janela.geometry(f"+{x}+{y}")

        label = tk.Label(
            self._janela, text=self.texto, justify="left",
            background="#333333", foreground="#ffffff",
            relief="solid", borderwidth=1,
            font=("Segoe UI", 9), padx=8, pady=4,
        )
        label.pack()

    def _esconder(self):
        if self._janela is not None:
            self._janela.destroy()
            self._janela = None