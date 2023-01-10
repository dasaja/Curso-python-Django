from calculadora_intermedia import CalculadoraIntermedia
class Operaciones:
    """Modelo de la calculadora"""
    def __int__(self, sumar, restar, producto, dividir):

        self.Sumar = sumar
        self.Restar = restar
        self.Multiplicar = producto
        self.Dividir = dividir

    def Sumar(self):
        n1 = float(input("Introduce el primer número: "))
        n2 = float(input("Introduce el segundo número: "))
        sumar = n1 + n2
        print("La Suma es = ", sumar)

    def Restar(self):
        n1 = float(input("Introduce el primer número: "))
        n2 = float(input("Introduce el segundo número: "))
        restar = n1 - n2
        print("La Resta es = ", restar)

    def Multiplicar(self):
        n1 = float(input("Introduce el primer número: "))
        n2 = float(input("Introduce el segundo número: "))
        producto = n1 * n2
        print("El Producto es = ", producto)

    def Dividir(self):
        n1 = float(input("Introduce el primer número: "))
        n2 = float(input("Introduce el segundo número: "))
        dividir = n1 / n2
        print("La División es = ", dividir)


    def Calculadora(self):
        fin = False
        while not(fin):


            print(f"""
        
        
            1. Sumar
            2. Restar
            3. Multiplicar
            4. Dividir
            5. Potencia
            6. Factorial
            7. Salir
        
             """)
            opcion = int(input("Ingresa tú opción: "))
            if opcion == 1:
                self.Sumar()

            elif opcion == 2:
                self.Restar()
            elif opcion == 3:
                self.Multiplicar()
            elif opcion == 4:
                self.Dividir()
            elif opcion == 5:
                C2 = CalculadoraIntermedia()
                C2.Potencia()
            elif opcion == 6:
                C3 = CalculadoraIntermedia()
                C3.Factorial()

            elif (opcion == 7):
                fin = 1
















