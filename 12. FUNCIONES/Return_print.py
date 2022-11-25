#Diferencia entre return y print
#uso del print 
def imprimir(a,b):
  print(a+b)

print(type(imprimir(5,5)))

#return 
def imprimir2(a,b):
  return a*b

r = imprimir2(2,4)
print(r)
print(type(imprimir2))


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

