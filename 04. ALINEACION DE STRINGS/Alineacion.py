#Alineacion, relleno y precision .format()
print('{0:8} | {1:9}'.format('Fruutas', 'Cantidad'))
print('{0:8} | {1:9}'.format('Manzanas', 3))
print('{0:8} | {1:9}'.format('Naranjas', 5))
print('{0:8} | {1:9}'.format('Peras', 10))

print("\n")

print('{0:=<8} | {1:-^8} | {2:.>8}'.format('Izquierda', 'Centro', 'Derecha'))
print('{0:=<8} | {1:-^8} | {2:.>8}'.format(12, 13, 15))

print("\n")

print("es un numero de diez caracteres y dos decimales: %10.2f"%13.57899699)


print('\n')

num = 23.45
print('Esre numero de 10 caracteres, cuatro decimales: {0:10.4f}'.format(num))
print(f"este numero de 10 caracteres y 4 decimales: {num:{10}.{6}}")

num2 = 12.25
print("10 caracteres, 4 decimales :{0:10.4f}".format(num2))

num2 = 12.25
print("10 caracteres, 4 decimales :{0:10.4f}".format(num2))

