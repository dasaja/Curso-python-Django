#Ejercicio Interacciones entre funciones
"""Menor de dos pares: escriba una función que devuelva el menor
de dos números dados si ambos números son pares, pero devuelva el 
mayor si uno o ambos números son impares.

menor_de_dos_pares(2,4) --> 2
mayor_de_dos_pares(2,5) --> 5"""

"""def num_par (num1, num2):
   
   if num1 % 2 == 0 and num1 < num2 :
   else:
     num2 
    return num1"""

def menor_de_dos_pares(a,b):
  if a%2 == 0 and b%2 == 0:
    return min(a,b)
  else:
    return max(a,b)

print(menor_de_dos_pares(2,4))
print(menor_de_dos_pares(1,6))



 