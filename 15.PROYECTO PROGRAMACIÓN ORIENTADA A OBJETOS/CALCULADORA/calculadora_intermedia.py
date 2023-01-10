class CalculadoraIntermedia():
    def __int__(self):
        pass

    def Potencia(self):
        base = float(input("Introduce el primer número: "))
        exponente = float(input("Introduce el segundo número: "))
        p = base ** exponente
        print("La Potencia es =", p)

    def Factorial(self):
        n = int(input("Introduce un número: "))
        if n >= 0:
            x = 1
            f = 1
            while x <= n:
                f = f * x
                x += 1
            print("EL Factorial de", n, "es =", f)
        else:
            print ("No se puede calcular el factorial")




