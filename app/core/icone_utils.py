import os
import sys

CAMINHO_LOGO_PNG = os.path.join(
    os.path.dirname(__file__), "..", "..", "assets", "logo.png"
)
CAMINHO_ICO = os.path.join(
    os.path.dirname(__file__), "..", "..", "assets", "icon.ico"
)

# tenta reaplicar o ícone várias vezes, pois o ttkbootstrap pode
# redefinir o ícone sozinho enquanto ainda está carregando o tema
_TENTATIVAS_MS = [50, 150, 300, 600, 1000, 1500, 2500]


def aplicar_icone(janela):
    """
    Aplica o ícone do Zeladoc na janela (título e, no Windows, na barra
    de tarefas). Deve ser chamado logo após a criação de cada
    ttk.Window/Toplevel.
    """
    janela.update_idletasks()
    for atraso in _TENTATIVAS_MS:
        janela.after(atraso, lambda j=janela: _definir_icone(j))


def _definir_icone(janela):
    try:
        if sys.platform.startswith("win") and os.path.exists(CAMINHO_ICO):
            janela.iconbitmap(default=CAMINHO_ICO)
        elif os.path.exists(CAMINHO_LOGO_PNG):
            from PIL import Image, ImageTk

            imagem = Image.open(CAMINHO_LOGO_PNG)
            icone = ImageTk.PhotoImage(imagem)
            janela.iconphoto(True, icone)
            janela._icone_taskbar_ref = icone
    except Exception:
        pass


def gerar_icone():
    from PIL import Image

    im = Image.open(CAMINHO_LOGO_PNG).convert("RGBA")

    lado = max(im.size)
    quad = Image.new("RGBA", (lado, lado), (0, 0, 0, 0))
    quad.paste(im, ((lado - im.size[0]) // 2, (lado - im.size[1]) // 2), im)

    tamanhos = [(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
    quad.save(CAMINHO_ICO, sizes=tamanhos)

    print(f"icon.ico criado em {os.path.abspath(CAMINHO_ICO)}")


if __name__ == "__main__":
    gerar_icone()