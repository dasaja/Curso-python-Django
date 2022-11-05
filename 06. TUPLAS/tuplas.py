#Tuplas 
#son inmutables 
valores = (1,2,3,4,5)
print(valores)

valores_mixtos = (1, "Hola", 2.5, False)
#podemos acceder a los valores
print(valores_mixtos[0])

#podemos hacer un slinsing 
print(valores_mixtos[2:4])

#unpack => desempaquetar valores 
var1, var2, var3, var4 = valores_mixtos
print(var3)