import tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack

#Crear nuesta app
myapp = App()

#Crear los métodos
myapp.master.title("Mi aplicación de Tareas")
myapp.master.maxsize(1000, 400)

#empieza la app
myapp.mainloop()