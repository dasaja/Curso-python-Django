
print("Fichero Inicial")
fLectura = open("archivo.txt", "r")
texto = fLectura.read()
fLectura.write("México")
print(texto)
fLectura.close()


#Escritura
fescritura = open("archivo.txt", "a")
fescritura.write("Ciudad: Guayaquil\n")
fescritura.write("55 grados")
fescritura.close()

#Lectura

"""fLectura = open("archivo.txt", "r")
texto = fLectura.read()
print(texto)
fLectura.close()"""

