"""
while test:
  code
else:
  final code 
"""
x = 0 

while x < 10:
  print('x es actualmente', x)
  print('x sigue siendo menor que 10, suma 1')
  x+=1



# break  => salir del bucle, presente valor
# continue => conitua con la iteracion a pesar de un error
# pass => No hace nada  

x = 0 

while x < 10:
  print("x es actualmente: ",x)
  x+=1
  if x == 3:
    print('x == 3')
    break
  else:
    print('conituara')
    continue

  
