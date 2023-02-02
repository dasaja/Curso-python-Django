import tkinter as tk
from cliente.gui import Frame, barra_menu


def main():
    root = tk.Tk()
    root.title("Catálogo de películas")
    root.iconbitmap("img/video.ico")
    root.resizable(0,0)  #da elasticidad tanto vertical como horizontal X, Y

    barra_menu(root)


    app = Frame(root=root)

    app.mainloop()

if __name__ == "__main__":
    main()