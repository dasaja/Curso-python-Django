"""
for v in range(especificacion):
    instruccion en el bloque P
    instruccion en el bloque P
    instruccion en el bloque P
    instruccion en el bloque P
"""

for n in range(1,6):
    m = n**2
    print('Numero: ', n, 'Cuadrado: ', m )
    

#calcule y muestre el promedio de un grupo de datos ingresados desde el teclado

n = int(input('Cantidad de datos: '))
s=0
for i in range(n):
    x = float(input('Ingrese el siguiente dato: '))
    s+=x
p=s/n
print('El promedio es: ', p)


#Dado un numero entero positivo, encunetre todos sus divisores enteros positivos.

n = int(input('Ingrese un entero positivo: '))
for d in range(1, n+1):
    if n%d==0:
        print('Divisor', d)


n = int(input('Ingresar un entero positivo: '))
c = 0
for d in range(1, n+1):
    if n%d==0:
        c += 1
if c>2:
    print(n,'No es primo')
else:
    print(n,'Si es primo')


print('Impares')
for i in range(1, 10, 2):
    print(i, end=', ')
    