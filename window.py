import tkinter as tk
from tkinter import scrolledtext
import time


class Ventana:

    def __init__(self, titulo, icono):
        self.ventana = tk.Tk()
        self.ventana.title(titulo)
        self.icono = self.ventana.iconbitmap(icono)

        # Variable
        # self.varInfo = tk.StringVar(values=self.arr)

        # 1. Lado izquierdo
        # 1.1 Frame
        self.frameIzq = tk.Frame(self.ventana)
        self.frameIzq.config(bg='#38184C', padx=30, pady=60)
        self.frameIzq.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        # 1.1.1 Canvas
        self.canva = tk.Canvas(self.frameIzq)
        self.canva.config(bg='#1F0802', width=300)
        self.canva.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # 2. Lado derecho
        # 2.1 Frame
        self.frameDer = tk.Frame(self.ventana)
        self.frameDer.config(bg='#38184C', padx=30, pady=60)
        self.frameDer.pack(fill=tk.Y, expand=True)
        # 2.1.1 Text
        self.textInfo = scrolledtext.ScrolledText(self.frameDer)
        self.textInfo.config(width=35,
                             bg='#A0CD60',
                             wrap=tk.WORD
                             # textvariable=self.varInfo
                             )
        self.textInfo.pack(fill=tk.Y, expand=True)
        # 2.1.2 Textbox
        self.entrada = tk.Entry(self.frameDer)
        self.entrada.config(bg='#CEF09D')
        self.entrada.pack(fill=tk.X, pady=20)
        # 2.1.3 Boton
        self.button = tk.Button(self.frameDer)
        self.button.config(bg='#CEF09D', text='Enter')
        self.button.pack(fill=tk.X)

        # 3. Mostrar informacion

    def escribir(self, frase):
        self.textInfo.config(state=tk.NORMAL)
        self.textInfo.insert(tk.END, frase)
        self.textInfo.see('end')
        self.textInfo.config(state=tk.DISABLED)
        self.frameDer.update_idletasks()

    def mostrar(self):
        self.ventana.mainloop()


# ventana = Ventana(
#     'Ahoracado', 'C:/Users/gferm/OneDrive/Escritorio/Programación/ahorcado/khangman_94222_peque.ico')

# arr = ['linea 1',
#        'linea 2']

# ventana.escribir(arr)


# arr.append('linea 3')

# ventana.escribir(arr)


# arr = ['linea 4',
#        'linea 5',
#        'linea 6',
#        'linea 7',
#        'linea 8',
#        'linea 9',
#        'linea 10']


# ventana.mostrar()
