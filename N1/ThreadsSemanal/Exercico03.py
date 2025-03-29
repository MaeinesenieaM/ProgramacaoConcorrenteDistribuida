from PIL import Image
from tkinter import Tk, filedialog

import threading
import queue

#Este valor do tipo Queue guarda a posição da imagem para que as threads possam usar.
image_x_positions = queue.Queue()

def converter_coluna(altura, imagem_original, imagem_final):
    coluna = image_x_positions.get()    #Pega uma coluna esperando a ser trabalhada na queue.
    for linha in range(altura):
        r, g, b = imagem_original.getpixel((coluna, linha))
        luminancia = int(0.299 * r + 0.587 * g + 0.114 * b)
        imagem_final.putpixel((coluna, linha), luminancia)  #Avisa que o trabalho foi concluído na coluna.
    image_x_positions.task_done()

def converter_para_preto_e_branco_manual():

    try:
        root = Tk()
        root.withdraw()

        caminho_imagem = filedialog.askopenfilename(
            title="Selecione uma imagem",
            filetypes=[("Imagens", "*.jpg *.jpeg *.png *.bmp *.gif"), ("Todos os arquivos", "*.*")]
        )

        if not caminho_imagem:
            print("Nenhuma imagem foi selecionada.")
            return

        imagem = Image.open(caminho_imagem)
        imagem = imagem.convert("RGB")  # Garante que a imagem esteja no modo RGB
        largura, altura = imagem.size
        imagem_preto_branco = Image.new("L", (largura, altura))

        # Itera sobre cada píxel da imagem
        for x in range(largura):
            #Aki é inserido a coluna da imagem a ser trabalhada nas threads e cria uma thread para realizar o trabalho.
            image_x_positions.put(x)
            threading.Thread(target = converter_coluna, args = [altura, imagem, imagem_preto_branco]).start()

        image_x_positions.join() #Espera que todos os elementos da Queue fiquem prontos.
        caminho_saida = filedialog.asksaveasfilename(
            title="Salvar imagem em preto e branco",
            defaultextension=".jpg",
            filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png"), ("Todos os arquivos", "*.*")]
        )

        if not caminho_saida:
            print("Operação de salvamento cancelada.")
            return

        # Salva a imagem em preto e branco no caminho especificado

        imagem_preto_branco.save(caminho_saida)
        print(f"Imagem convertida com sucesso! Salva em: {caminho_saida}")

    except Exception as e:
        print(f"Erro ao processar a imagem: {e}")

# Exemplo de uso

if __name__ == "__main__":
    converter_para_preto_e_branco_manual()