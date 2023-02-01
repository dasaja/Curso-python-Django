from tkinter import ttk
from tkinter import *

root = Tk() #Creación del Objeto

frm = ttk.Frame(root, width=100, height=100)
frm.grid()
ttk.Label(frm, text="Hola Mundo").grid(column=0, row=0) #grid(son las lineas de las columnas y filas) quiere decir que trabaja en filas y columnas
ttk.Button(frm, text="salir", command=root.destroy).grid(column=1, row=0)

root.mainloop() #Cierra el ciclo
