#Alcance de las variables = Existe locales y globales
nombre = "Jose" #variable global

def primo(n):
  c=0 #variable local
  for i in range(1, n+1):
    if n%i==0:
      c = c + 1

  if c>2:
    return False
  else:
    return True

#llamamos la funcion
print(nombre)
a = int(input('desde: '))
b = int(input('hasta: '))
for n in range(a,b+1):
  if primo(n):
    print('Numero primo: ', n)