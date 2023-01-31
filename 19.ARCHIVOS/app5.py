#Escribir de python al texto.
f = open("archivo.txt", "r")
lineas = f.readlines()
f.close()

fescritura = open("archivo.txt", "a")
fescritura.write("Cuenca\n")

print(lineas[0])
print(lineas[3])
