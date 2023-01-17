#Escribir una función que calcule 
# el volumen de una esfera dado su radio
"""def volumen (a,b,π,r):
    PI = 3.14
    volumen = (a/b)(*π)(*r**3)
    return Volumen

print (volumen(4/3)*3,14*4**3)"""

#Respuesta del profesor 

"""def vol(rad):
  return (4/3)*(3.14)*(rad**3)

print(vol(2))"""

#Escribir una función que verifique si un númer está en un rango
#(Incluye el valor alto y bajo) 5,2,7
#Resultado :
#check(5,2,7) 5 está en el rango entre 2 y 7

"""def rango (a,b,c):
    if  a<b or a>b and c<b or c>b :
        print (b, "Esta en el rango entre", a "y", c)
        return
    elif b<a or b>a and c<a or c>a:
        print (a, "Esta en el rango entre", b "y", c)
    elif c<b or c>b and c<a or c>a: 
        return  """

#PROFESOR
"""def rango_check(num,bajo,alto):
    if num in range(bajo,alto+1):
        print('{} esta en el rango entre {} y {}'.format(num,bajo,alto))
    else:
        print('El numero esta fuera del rango.')


rango_check(9,8,2)"""

#Escribir una función que acepte una cadena y calcule el 
#número de letras mayúsculas y minisculas
#s= "Hola como estás en Ecuador"
#Resultado: cadena(S)
#minusculas = 5 
#mayusculas = 2

"""def cadenas (s):
    s= "Hola como estás en Ecuador"
    if len.upper in s:
        print (int(s))
    else:
        return print(len.lower (int(s)))

print(cadenas)  """

#PROFERSOR
"""def cadenas(s):
  d={"upper":0, "lower":0}
  for c in s:
    if c.isupper():
      d["upper"]+=1
    elif c.islower():
      d["lower"]+=1
    else:
      pass 

  print("String original : ", s)
  print("Total de mayusculas: ", d["upper"])
  print("Total de minusculas: ", d["lower"])

s = "Hola como estas Ecuador"
cadenas(s)"""

#Escriba una función que tome una lista y devuelva una nueva
#lista con elementos únicos de la primera lista
#lista_muestra = [1,1,1,1,2,2,3,3,3,4,4,5,5,]
#lista_muestra = [1,2,3,4,5]

"""def lista_muestra (lista):
    x= """

#Profesor
"""def lista_unica(lst):
  x = []
  for a in lst:
    if a not in x:
      x.append(a)
  return x 

print(lista_unica([1,1,1,1,2,2,3,3,3,3,4,5]))"""
#Escriba una función que permita multiplicar todos los números de una lista
#Lista_muestra = [1,2,3,-4]
# resultado = -24

"""def lista_muestra(x,y,*args):
    return lista_muestra (x* y* args[0] * args[1])




print(lista_muestra(1,2,3,-4))"""

"""def lista_muestra(*args):
   return args

print(lista_muestra(1*2*3*-4*2*2))

#Profesor
def multiplicar(nums):
  total = 1
  for x in nums:
    total *= x
  return total


print(multipicar([1,2,3,-4,2]))"""


#Escriba una función que verifique si una palabra o frase
#es palindromo
#palindromo ("asadd") True o False 

"""def palindromo (palabra):
    if palindromo == palabra [::-1]:
        print (True)
    else:
        return (False)    

print(palindromo("Ana")) """       

#Profesor
def palindromo(s):
  s = s.replace(' ','')
  return s == s[::-1]

print(palindromo('zorra - arroz'))
print(palindromo('comer'))