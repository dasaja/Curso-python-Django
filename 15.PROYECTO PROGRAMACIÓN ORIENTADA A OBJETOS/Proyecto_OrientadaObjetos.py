def Sumar (x, y):
    sumar = x + y
    print(sumar)

def Restar( x, y):
    restar = x - y
    print(restar)

def Multiplicar( x, y):
    producto = x * y
    print(producto)

def Dividir( x, y):
    dividir = x / y
    print(dividir)

def Calculadora(self):
        opcion = 0
        while opcion != 5:
            print(f"""
        
        
            1. Sumar 
            2. Restar
            3. Multiplicar
            4. Dividir
            5. Salir
        
             """)

            opcion = int(input("Ingresa tú opción"))

            n1 = float(input("Introduce el primer número: "))
            n2 = float(input("Introduce el segundo número: "))

            if opcion == 1:
                print("")
                print("La suma es ", self.Sumar(n1 + n2))
            elif opcion == 2:
                print("La resta es", self.Restar(n1-n2))
            elif opcion == 3:
                print("El producto es", self.Multiplicar(n1*n2))
            elif opcion == 4:
                print("La división es", self.Dividir(n1/n2))
            elif opcion == 5:
                print("---Salir---")
                break
            else:
                print("Error, intenta nuevamente")

print()

