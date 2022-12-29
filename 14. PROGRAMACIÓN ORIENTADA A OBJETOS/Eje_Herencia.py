class Persona:
    def __init__(self):
        self.__Nombre = ""
        self.__Apellidos = ""
        self.__Edad = 0

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


class Alumno(Persona):
    def __init__(self):
        super().__init__()
        self.__Curso = ""
        self.__Asignaturas = ""

    def getCurso(self):
        return self.__Curso
    def setCurso(self, curso):
        self.__Curso = curso

    def getAsignaturas(self):
        return self.__Asignaturas
    def setAsignaturas(self, asignaturas):
        self.__Asignaturas = asignaturas

    def MostrarAlumno(self):
        print("Alumno")
        print("\tNombre", self.getNombre())
        print("\tApellidos", self.getApellidos())
        print("\tEdad", self.getEdad()) 
        print("\tCurso", self.__Curso)
        print("\tMatriculas", self.__Asignaturas)    

alumno = Alumno()
alumno.setNombre("Daniel")
alumno.setApellidos("Salcedo")
alumno.setEdad(30)
alumno.setCurso("Bachillerato")
alumno.setAsignaturas(["Matematicas", "Fisica", "Programación"])
alumno.MostrarAlumno()          

#Antiguedad, tutorias, Teléfono (Privados)

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

    def MostrarProfesor (self):
        print("Profesor")
        print("\tNombre", self.getNombre())
        print("\tApellidos", self.getApellidos())
        print("\tEdad", self.getEdad()) 
        print("\tAntiguedad", self.__Antiguedad)
        print("\tTutorias", self.__Tutorias)  
        print("\tTeléfono", self.__Teléfono)       



profesor = Profesor ()
profesor.setNombre("Daniel")
profesor.setApellidos("Salcedo")
profesor.setEdad(30)
profesor.setAntiguedad(15)
profesor.setTutorias([["Lunes", "16-18"], ["Jueves", "12-14"], ["Viernes" , "13-14"]])
profesor.setTelefono("785693")
profesor.MostrarProfesor()            