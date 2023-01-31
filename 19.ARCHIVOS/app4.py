#Leer solo por líneas una o más con slide [:]

f = open("archivo.txt", "r")
lineas = f.readlines()
f.close()

print(lineas[0])
print(lineas[3])



