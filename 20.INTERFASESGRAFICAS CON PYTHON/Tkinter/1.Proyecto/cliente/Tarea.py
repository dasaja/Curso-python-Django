import tkinter as tk
from tkinter import ttk

def barra_menu2(root):
    barra_menu2 = tk.Consultas(root)
    root.config(menu=barra_menu2, width=300, height=300)

    menu_consultas = tk.Consultas(barra_menu2, tearoff=0)
    barra_menu2.add_cascade(label="Consultas", consultas=menu_consultas)



class Frame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=480, height=320)
        self.root = root
        self.pack()
        self.config(bg="green")


