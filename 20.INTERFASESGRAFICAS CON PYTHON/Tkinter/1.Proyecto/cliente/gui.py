import tkinter as tk
from tkinter import ttk


def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu=barra_menu, width=300, height=300)

    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Inicio", menu=menu_inicio)

    menu_consultas = tk.Menu(barra_menu)
    barra_menu.add_cascade(label="Consultas", menu=menu_consultas)

    menu_configuracion = tk.Menu(barra_menu)
    barra_menu.add_cascade(label="Configuración", menu=menu_configuracion)

    menu_ayuda = tk.Menu(barra_menu)
    barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

    "Sub Menús"
    menu_inicio.add_command(label="Crear registro en DB")
    menu_inicio.add_command(label="Eliminar registro en la DB")
    menu_inicio.add_command(label="Salir", command=root.destroy)


class Frame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=480, height=320)
        self.root = root
        self.pack()
        self.config(bg="green")

        self.campos_pelicula()
        self.deshabilitar_campo()
        self.tabla_peliculas()

    def campos_pelicula(self):
        # Labels de cada campo
        self.label_nombre = tk.Label(self, text="Nombre: ")
        self.label_nombre.config(font=("Arial", 12, "bold"))
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)

        self.label_duracion = tk.Label(self, text="Duración: ")
        self.label_duracion.config(font=("Arial", 12, "bold"))
        self.label_duracion.grid(row=1, column=0, padx=10, pady=10)

        self.label_genero = tk.Label(self, text="Género: ")
        self.label_genero.config(font=("Arial", 12, "bold"))
        self.label_genero.grid(row=2, column=0, padx=10, pady=10)


        #Entry de cada campo
        self.mi_nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable=self.mi_nombre)
        self.entry_nombre.config(width=50, font=("Ariel", 12),)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

        self.mi_duracion = tk.StringVar()
        self.entry_duracion = tk.Entry(self, textvariable=self.mi_duracion)
        self.entry_duracion.config(width=50, font=("Ariel", 12))
        self.entry_duracion.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

        self.mi_genero = tk.StringVar()
        self.entry_genero = tk.Entry(self, textvariable=self.mi_genero)
        self.entry_genero.config(width=50, font=("Ariel", 12))
        self.entry_genero.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

        #Botones

        self.boton_nuevo = tk.Button(self, text="Nuevo", command=self.habilitar_campo)
        self.boton_nuevo.config(width=20, font=('Arial', 12, 'bold'),
                                fg='#DAD5D6', bg='#158645',
                                cursor='hand2', activebackground='#35BD6F')
        self.boton_nuevo.grid(row=3, column=0, padx=10, pady=10)

        #Boton Guardar
        self.boton_guardar = tk.Button(self, text="Guardar")
        self.boton_guardar.config(width=20, font=('Arial', 12, 'bold'),
                                fg='#DAD5D6', bg='#1658A2',
                                cursor='hand2', activebackground='#3586DF')
        self.boton_guardar.grid(row=3, column=1, padx=10, pady=10)


        #Boton Cancelar
        self.boton_cancelar = tk.Button(self, text="Cancelar")
        self.boton_cancelar.config(width=20, font=('Arial', 12, 'bold'),
                                  fg='#DAD5D6', bg='#BD152E',
                                  cursor='hand2', activebackground='#E15370')
        self.boton_cancelar.grid(row=3, column=2, padx=10, pady=10)


        #Validaciones de campos | Entries
        #Deshabilitar campo
    def deshabilitar_campo(self):
        self.mi_nombre.set("")
        self.mi_duracion.set("")
        self.mi_genero.set("")

        self.entry_nombre.config(state="disable")
        self.entry_duracion.config(state="disable")
        self.entry_genero.config(state="disable")

        self.boton_guardar.config(state="disable")
        self.boton_cancelar.config(state="disable")

    def habilitar_campo(self):
        self.mi_nombre.set("")
        self.mi_duracion.set("")
        self.mi_genero.set("")

        self.entry_nombre.config(state="normal")
        self.entry_duracion.config(state="normal")
        self.entry_genero.config(state="normal")

        self.boton_guardar.config(state="normal")
        self.boton_cancelar.config(state="normal")

    def tabla_peliculas(self):

        self.tabla = ttk.Treeview(self, column=("Nombre", "Duracion","Genero"))
        self.tabla.grid(row=4, column=0, columnspan=4)

        #Scroball
        self.scroll = ttk.Scrollbar(self, orient="vertical", command=self.tabla.yview)
        self.scroll.grid(row=4, column=4, sticky="nse")
        self.tabla.configure(yscrollcommand=self.scroll.set)

        #Crear títulos | Cabeceras o Heading
        self.tabla.heading("#0", text="ID")
        self.tabla.heading("#1", text="Nombre")
        self.tabla.heading("#2", text="Duración")
        self.tabla.heading("#3", text="Género")












