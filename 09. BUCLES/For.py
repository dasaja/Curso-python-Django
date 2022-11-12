""""
    for item in object:
        operacion
"""

lista = [1,2,3,4,5,6,7,8,9,10]

#for item in lista:
   #print(item)

for num in lista:
    if num % 2 == 0:
        print(num)
    else:
        print("Impar" , num)
        

"""
Leer el numero de llantas de una compra y mostrar el valor qeu debe pagarse.El alamacen las vende con la siguiente politica: Si se compra menos de 5 llantas, el precio es unitario es 80. Si se compra 6 o 7 , el precio unitario es de 70, y si se compra mas de 7 llantas, el precio es de $60 
"""
n = int(input('Cantidad de llantas: '))
if n < 5:
    p = 80
elif n==6 or n==7:
    p = 70
else:
    p = 60

t = n * p 
print('Valor a pagar: ', t)





"""for item in secuencia
    intrucciones de bloque 
    intrucciones de bloque 
    intrucciones de bloque 
    intrucciones de bloque
"""


lista = [1,2,3,4,5,6,7,8,9,10]

lista_sum =0

for p in lista:
    lista_sum += p 

print(lista_sum)

#Lista con tuplas
lista = [(2,4),(6,8),(10,12)]

for tup in lista:
    print(tup)

for (t1,t2) in lista:
    print(t2)


#diccionarios

d = {'k1':1, 'k2':2, 'k3':3}

print(list(d.keys()))
print(list(d.values()))

for k,v in d.items():
    print(k)
    print(v)

#Iterar
for letras in "Este es un string":
    print(letras)



#Generador de contrasenas
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Bienvenido a mi PyPaswword Generator!")
nr_letters = int(input("Cuantas letras quieres en tu contrasena?\n"))
nr_symbols = int(input('Cuantos simbolos quieres?\n'))
nr_numbers = int(input('Cuantos numeros quieres?\n'))

password_list = []
for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Tu contrasena es: {password}")

