#ELSE => se ejecuta si la condicion no se cumple

numero = 20
if numero > 10:
  #si se cumple la condicion se ejecuta esta parte
  print("Es mayor a diez")
else:
  #si no se cumple la condicion se ejecuta esta parte 
  print("Es menor o igual a diez")


""""
Para le pago semanal a un obrero se ocnsidere los siguientes datos:
horas_trabajadas, tarifa por hora y descuentos
Si la cantidad de horas trabajdas en la semana es mayor a 40, se le debe pagar las horas en exceso con una bonificacion de 50% adiconal al pago normal.
"""

c = float(input("Horas trabajadas: "))
t = float(input("Tarifa por hora: "))
d = float(input("Descuentos ")) 

if c<=40:
    p=c*t - d 
else:
    p=40*t + 1.5*t*(c - 40) - d 

print('Valor a pagar', p)



persona = 'Daniel Salcedo'

if persona == 'jose':
    print(f'Bienvenido {persona}')
elif persona == 'Daniel':
    print(f'Bienvenido {persona}')
else:
    print("Bienvenida , Cual es tu nombre?")