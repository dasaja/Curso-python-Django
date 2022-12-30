class Persona:
    def __init__(self):
        self.__Nombre = ""
        self.__Apellidos = ""
        self.__Edad = ""

    def getNombre(self):
        return self.__Nombre

    def setNombre(self, nombre):
        self.__Nombre = nombre        

    def getApellidos(self):
        return self.__Apellidos

    def setApellidos(self, apellidos):
        self.__Apellidos = apellidos

    def getEdad(self):
        return self.__Edad

    def setEdad(self, edad):
        self.__Edad = edad   


class Profesor(Persona):
    def __init__(self) :
        super().__init__()
        self.__Antiguedad = ""
        self.__Tutorias = ""
        self.__Teléfono = ""

    def getAntiguedad (self):
        return self.__Antiguedad
    def setAntiguedad (self,antiguedad):
        self.__Antiguedad = antiguedad

    def getTutorias(self):
        return self.__Tutorias
    def setTutorias(self, tutorias):
        self.__Tutorias = tutorias

    def getTelefono(self):
        return self.__Teléfono
    def setTelefono(self,telefono):
        self.__Teléfono = telefono 


class Investigador(Persona):
    def __init__(self):
        super().__init__()
        self.__Especialidad = ""
        self.__Años = ""

    def getEspecialidad(self):
        return self.__Especialidad
    def setEspecialidad (self, especialidad):
        self.__Especialidad = especialidad

    def getAños(self):
        return self.__Años
    def setAños(self, años):
        self.__Años = años

   

class ProUniversitario(Profesor,Investigador): 
    def __init__(self):
         super().__init__()
         self.__Universidad = ""
         self.__Departamento = ""

    def getUniversidad(self):
        return self.__Universidad
    def setUNiversidad(self,universidad):
        self.__Universidad = universidad       

    def getDepartamento(self):
        return self.__Departamento
    def setDepartamento (self, departamento):
        self.__Departamento = departamento

    def MostrarProUniversitario(self):
       
        print("\n" "Profesor Universitario" )
        print("\tNombre", self.getNombre())
        print("\tApellidos",self.getApellidos())
        print("\tEdad",self.getEdad())
        print("\tAntiguedad", self.getAntiguedad())
        print("\tTutorías", self.getTutorias())
        print("\tTeléfono", self.getTelefono())
        print("\tEspecialidad", self.getEspecialidad())
        print("\tAños", self.getAños())
        print("\tUniversitario", self.__Universidad)
        print("\tDepartamento", self.__Departamento)

profesor = ProUniversitario()
profesor.setNombre("Jose")
profesor.setApellidos("Diaz")
profesor.setEdad(50)
profesor.setAntiguedad(15)
profesor.setTutorias([["Lunes","16-18"], ["Jueves","12-14"], ["Viernes","11-13"]])
profesor.setTelefono("895623")
profesor.setEspecialidad("Desarrollo de Software")
profesor.setAños(15)
profesor.setUNiversidad("Universidad de Barcelona")
profesor.setDepartamento("Lenguajes y Sistemas Informaticos")
profesor.MostrarProUniversitario()

#Profesor 2
("\n")
profesor2 = ProUniversitario()
profesor2.setNombre("Daniel")
profesor2.setApellidos("Salcedo")
profesor2.setEdad(30)
profesor2.setAntiguedad(3)
profesor2.setTutorias([["Lunes","16-17"], ["Jueves","12-15"], ["Viernes","11-13"]])
profesor2.setTelefono("25895623")
profesor2.setEspecialidad("Comunicación")
profesor2.setAños(5)
profesor2.setUNiversidad("Universidad de Nacional")
profesor2.setDepartamento("Telecomunicaciones")
profesor2.MostrarProUniversitario()





