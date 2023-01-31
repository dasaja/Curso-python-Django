#Leer solo por líneas una o más

f = open("archivo.txt", "r")
print(f.readline())
print(f.readline())
print(f.readline())


f.close()