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
        print("Impar" int(num))
        

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

