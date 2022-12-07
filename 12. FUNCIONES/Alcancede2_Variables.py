#Scope
#Regla 1. Las asignaciónes de nombre crean o cambian los nombres locales
#Regla 2. Referencias de nombres: 
"""
-Local
-Asignado en una función 
-Variable Global 
-Variable incorporada
"""
#Regla 3. Los nombres declarados en declaraciones globales y no locales asignan en ambito a funciones y módulos.

x = 25

def imprimir ():
    x = 50
    return x

#Se ejecuta x = 25    
print(x)

#Se ejecuta x = 50
print(imprimir())    

#Ejercicio
#Local - x es local 
f = lambda x: x**2
print(f(9))

#Variables locales en funciones (Bloques de código)

#Variable global
name = "Soy Gobal"
def saludar ():
    #Enclosing funtion
    name = "Jose"

def hola():
    print("Hola",name)

hola()
saludar()

print(name)

#Built-in
#Funciones definidas en python
len()


