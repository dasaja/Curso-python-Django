import tkinter as tk
from tkinter import ttk

def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu=barra_menu, width=300, height=300)

    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Inicio", menu=menu_inicio)

    menu_consolas = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Consolas", menu=menu_consolas)

    menu_configuracion = tk.Menu(barra_menu)
    barra_menu.add_cascade(label="Configuración", menu=menu_configuracion)

    menu_ayuda = tk.Menu(barra_menu)
    barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)


    "Sub Menús"
    menu_inicio.add_command(label="Crear registro en DB")
    menu_inicio.add_command(label="Eliminar registro en la DB")
    menu_inicio.add_command(label="Salir", command=root.destroy)

    menu_consolas.add_command(label="Crear registro en DB")
    menu_consolas.add_command(label="Eliminar registro en la DB")
    menu_consolas.add_command(label="Salir", command=root.destroy)

class Frame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=480, height=320)
        self.root = root
        self.pack()
        self.config(bg="green")

