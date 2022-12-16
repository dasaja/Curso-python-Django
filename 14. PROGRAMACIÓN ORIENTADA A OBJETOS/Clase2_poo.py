# Las clases son como moldes.
"""class Persona:
    def __init__(self, nombre, apellido, edad):#se lo conoce como constructor, primer método que se ejecuta un objeto de tipo persona
        self.Nombre = nombre
        self.Apellido = apellido
        self.Edad = edad

    def MostrarPersona(self):
        print("Nombre:" + self.Nombre)
        print("Apellidos:" + self.Apellido)
        print("Edad:" + str(self.Edad))

#Crear un objeto
p1 = Persona("José", "Díaz",30)
p2= Persona("Daniel", "Salcedo", 32)        
p1.MostrarPersona()
p2.MostrarPersona()"""


#EJercicio ,marca, modelo, color

class Telefono:
    #Constructor, el primero en empezar cuando se inicia el objeto
    def __init__(self, marca, modelo, color, precio):
        self.Marca = marca
        self.Modelo = modelo
        self.Color = color
        self.Precio = precio


    #Función 
    def Caracteristicas_Telefono(self):
        print("Marca:" + self.Marca)    
        print("Modelo:" + self.Modelo)
        print("Color:" + self.Color)
        print("Precio:" + str(self.Precio))

    def Origen_Telefono1(self):
        print("Estados Unidos")

    def Origen_Telefono2(self):
        print("Europa")    

    def Origen_Telefono3(self):
        print("Asia")    
     
 

#Crear Objeto
t1 = Telefono("Samsung","Ultra","Negro", "$1200")

t2 = Telefono ("Nokia", "1100", "Gris", "$150")
t3 = Telefono ("Motorola", "Rokect", "Azul Obscuro", "$250")

t1.Caracteristicas_Telefono()
t1.Origen_Telefono1()
print("\n")

t2.Caracteristicas_Telefono()
t2.Origen_Telefono2()
print("\n")

t3.Caracteristicas_Telefono()
t3.Origen_Telefono3()



        
   
  
