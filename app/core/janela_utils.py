import sys
import ctypes


def maximizar_respeitando_taskbar(janela):
   
    if sys.platform.startswith("win"):
        try:
            SPI_GETWORKAREA = 0x0030

            class RECT(ctypes.Structure):
                _fields_ = [
                    ("left", ctypes.c_long),
                    ("top", ctypes.c_long),
                    ("right", ctypes.c_long),
                    ("bottom", ctypes.c_long),
                ]

            area = RECT()
            ctypes.windll.user32.SystemParametersInfoW(
                SPI_GETWORKAREA, 0, ctypes.byref(area), 0
            )

            largura = area.right - area.left
            altura = area.bottom - area.top
            janela.geometry(f"{largura}x{altura}+{area.left}+{area.top}")
            return
        except Exception:
            pass

    janela.state("zoomed")


def bloquear_minimizar(janela):
   
    GWL_STYLE = -16
    WS_MINIMIZEBOX = 0x00020000

    if sys.platform.startswith("win"):
        try:
            janela.update_idletasks()
            hwnd = ctypes.windll.user32.GetParent(janela.winfo_id())
            estilo_atual = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_STYLE)
            ctypes.windll.user32.SetWindowLongW(
                hwnd, GWL_STYLE, estilo_atual & ~WS_MINIMIZEBOX
            )
        except Exception:
            pass

   
    def _ao_minimizar(event):
        if janela.state() == "iconic":
            janela.after(10, janela.deiconify)
            janela.after(50, lambda: maximizar_respeitando_taskbar(janela))

    janela.bind("<Unmap>", _ao_minimizar)