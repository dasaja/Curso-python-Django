"""
2. Dada una oración, devolver una oración con palabras
invertidas.
=====Resultado por consola
inversión_palabras("Estoy en casa") => "casa en Estoy"
inversión_palabras ("Voy a jugar") => "jugar a voy"
"""

"""def inversion_palabras(Frase ):
    #El split permite que quite espacios y el -1 permite invertir la frase.
  return " ".join(Frase.split()[::-1])

print(inversion_palabras("voy a jugar")) """

"""  return name[0:0].capitalize() + name[:4].upper() """

"""
3. Dado un número entero n, devuelve True si n está
dentro de 10, 100 o 200
=======Resultado por consola
numero_entero(90) ==>True
numero_entero(150) ==>False
===abs(num) retornar el valor absoluto de un número 
"""
#Ejercicio por resolver
"""def numero_entero(n):
    if n >= 10 and n <= 100 and n<= 200:
        return print (True)
    else:
        print(False)

print(numero_entero(90))
print(numero_entero(150))"""

#Ejercicio resuelto Valor absoluto
"""def numero_entero(n):
  return ((abs(100 - n) <= 10) or (abs(200 - 150) <= 10))
                  
print(numero_entero(90)) 
print(numero_entero(150))"""

#Actividad
"""
4. Dada una cadena devuelve una cadena donde por cada 
caracter en el original generemos tres caracteres más.
cadena_triple("Hola") ==> "HHHooolllaaa"
"""
def cadena_triple(text):
  result = ''
  for char in text:
    result += char * 3
  return result 

print(cadena_triple('Hola'))
print(cadena_triple('Jose'))

