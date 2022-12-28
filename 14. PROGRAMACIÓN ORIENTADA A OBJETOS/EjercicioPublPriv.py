class PersonaPublica:
    def __init__(self, nombre, apellidos, edad):
        self.Nombre = nombre
        self.Apellidos = apellidos
        self.Edad = edad

class PersonaPrivada:
    def __init__(self, nombre, apellidos, edad):
        self.__Nombre = nombre
        self.__Apellidos = apellidos 
        self.__Edad = edad     

    def GetNombre(self):
        return self.__Nombre 
    def SetNombre(self, nombre):
        self.__Nombre = nombre        

    def GetApellidos(self):
        return self.__Apellidos
    def SetApellidos(self, apellidos):
        self.Apellidos = apellidos

    def GetEdad(self):
        return self.__Edad
    def SetEdad(self, edad):
        self.__Edad = edad
    
#Creación de Obejtos Público y Privado
publico = PersonaPublica ("Daniel" , "Salcedo" , "35")
privado = PersonaPrivada ("Jose" ,"Diaz" , "28" )

print("Person Publica")
print("Nombre:" + publico.Nombre)
print("Apellidos:" + publico.Apellidos)
print("Edad:" + str(publico.Edad))

print("\n")

print("Persona Privada")
print("Nombre:" + privado.GetNombre())
print ("Apellidos" + privado.GetApellidos())
print ("Edad" + str(privado.GetEdad()))




