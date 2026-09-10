import tkinter as tk

class Menu_Principal_View:

    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("ZELADOC")
        self.janela.geometry("300x250")

        tk.Label(self.janela, text="=== ZELADOC ===", font=("Arial", 14)).pack(pady=10)

        tk.Button(self.janela, text="Pacientes", command=self.abrir_pacientes, width=20).pack(pady=5)
        tk.Button(self.janela, text="Médicos", command=self.abrir_medicos, width=20).pack(pady=5)
        tk.Button(self.janela, text="Consultas", command=self.abrir_consultas, width=20).pack(pady=5)
        tk.Button(self.janela, text="Sair", command=self.janela.destroy, width=20).pack(pady=5)

    def abrir_pacientes(self):
        print("Abrir tela de pacientes")  # depois vira uma chamada real ao controller

    def abrir_medicos(self):
        print("Abrir tela de médicos")

    def abrir_consultas(self):
        print("Abrir tela de consultas")

    def iniciar(self):
        self.janela.mainloop()