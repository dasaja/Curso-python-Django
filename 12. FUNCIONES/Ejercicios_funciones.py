from math import*

def area_circulo(r):
  s = pi*r**2
  return s

def sector(r,a):
  s = pi*r**2*a
  return s 

def segmento(r,a):
  s= r**2*(pi*a-0.5*sin(a))
  return s

def esfera(r):
  s = 4*pi*r**2
  v = 4*pi*r**3/3
  return [s, v]

def cilindro(r,h):
  s = 2*pi*r*(r+h)
  v = pi*r**2*h 
  return [s, v]

def cono(r, h):
  g = sqrt(h**2+r**2)
  s = pi*r+g+pi*r**2
  v = pi*r**2*h/3
  return [s,v]

s = area_circulo(2)
print(s)

r = cilindro(4 , 5)
print(r)


#Verifvar valores primos
#verificar valores primos
def primo(n):
  c=0
  for i in range(1, n+1):
    if n%i==0:
      c = c + 1

  if c>2:
    return False
  else:
    return True

#llamamos la funcion
a = int(input('desde: '))
b = int(input('hasta: '))
for n in range(a,b+1):
  if primo(n):
    print('Numero primo: ', n)


    
#funcion sin parámetros    
def menu():
  print('1) Ingresar dato')
  print('2) Mostrar resultado')
  print('3) Salir')


print(menu())




#Ejercicio de función en horas
#determina cual empleado tiene mas horas de trabajo

horas_trabajas = [('Daniel',200),('Maria',300),('Jose',400),('Elana', 1000)]

def empleado_check(horas_trabajas):
  max_horas = 0
  empleado_del_mes = ''

  for empleado, horas in horas_trabajas:
    if horas>max_horas:
      max_horas = horas
      empleado_del_mes = empleado
    else:
      pass

  return(empleado_del_mes, max_horas)

print(empleado_check(horas_trabajas))


