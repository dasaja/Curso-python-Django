div = 0
try:
   a = int(input("Ingrese el dividendo: "))
   b = int(input("Ingrese el divisor: "))

   div = a/b
except ValueError:
    print("Error: Ingrese solo número enteros!")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero!")
except Exception as error:
    print("Ha ocurrido un error no previsto", type(error).__name__)

print("La división es: ", div)



"""#Scope - alcance de variables
#global
num = 0
def contador():
    #local
    num = 0

suma = num"""