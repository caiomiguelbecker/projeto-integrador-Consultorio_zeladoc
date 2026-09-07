import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class Menu_Principal_View:

    def __init__(self):
        self.janela = ttk.Window(themename="flatly")
        self.janela.title("ZELADOC")
        self.janela.geometry("300x280")

        ttk.Label(self.janela, text="ZELADOC", font=("Arial", 18, "bold")).pack(pady=15)

        ttk.Button(self.janela, text="Pacientes", command=self.abrir_pacientes, bootstyle=PRIMARY, width=20).pack(pady=6)
        ttk.Button(self.janela, text="Médicos", command=self.abrir_medicos, bootstyle=PRIMARY, width=20).pack(pady=6)
        ttk.Button(self.janela, text="Consultas", command=self.abrir_consultas, bootstyle=PRIMARY, width=20).pack(pady=6)
        ttk.Button(self.janela, text="Sair", command=self.janela.destroy, bootstyle=DANGER, width=20).pack(pady=6)

    def abrir_pacientes(self):
        from app.views.paciente_view import Paciente_View
        Paciente_View(self.janela)

    def abrir_medicos(self):
        from app.views.medico_view import Medico_View
        Medico_View(self.janela)

    def abrir_consultas(self):
        from app.views.consulta_view import Consulta_View
        Consulta_View(self.janela)

    def iniciar(self):
        self.janela.mainloop()