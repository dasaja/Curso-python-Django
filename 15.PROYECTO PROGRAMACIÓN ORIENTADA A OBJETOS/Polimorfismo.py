class Persona:
    def __init__(self, nombre):
        self.Nombre = nombre

    def avanza(self):
        print("Ando caminando")

class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)     

    def avanza(self):
        print ("Ando en bicicleta")

def main(): #Funciones especiales python
    persona = Persona("Fabian")
    print(persona.Nombre)
    persona.avanza()     

           

    ciclista = Ciclista("Daniel")
    print(ciclista.Nombre)
    ciclista.avanza()

if __name__ == "__main__" :
    main ()






