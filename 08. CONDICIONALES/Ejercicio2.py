""" Solicitar al usuario que ingrese dos números y mostrar cuál de los dos es menor. Considerar el caso en que ambos números son iguales."""

Num1 = (input("Ingrese primer número: "))
Num2 = (input("Ingrese segundo número: "))

if Num1 < Num2:
    print("El primer número es el menor")
    
elif Num2 < Num1:
    print("El segundo número es el menor") 

elif Num1 == Num2:

    print("Ambos números son iguales")    