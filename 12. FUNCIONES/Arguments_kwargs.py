"""
*args-**kwargs
"""

#def myFuncion(a=0,b=3 ):
#    return sum((a,b))*0.5

#print(myFuncion(40,60))    

"""def miFuncion(*args): #El * permite reconocerlos como arguments
    return sum(args)*0.5

print(miFuncion(10,20,30,40,30)) """  

#Ejercicio 1

def multiplicar(*num):
    return multiplicar( num[0] * num[1])
   

print(multiplicar(10,20,30,40,))



#Kwargs
"""def miFuncion(**kwargs):
  if 'fruta' in kwargs:
    print(f"mi fruta favorita es {kwargs['fruta']}")
  else:
    print("No hay frutas")


print(miFuncion(fruta="uvas"))"""

