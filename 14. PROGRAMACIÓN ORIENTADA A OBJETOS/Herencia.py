class Persona:
    def __init__(self):
        self.__nombre = ""
        self.__apellido = ""
        self.__edad = 0
    
    def GetNombre(self):
        return self.__nombre

    def SetNombre(self, nombre):
        self.__nombre = nombre

    def GetApellido(self):
        return self.__apellido

    def SetNombre(self, apellido):
        self.__apellido = apellido

    def GetEdad(self):
        return self.__edad

    def SetEdad(self, edad):
        self.__edad = edad     

class Alumno (Persona):
    def __init__(self):
        super().__init__()
        self.__curso = ""
        self.__asignatura = ""

    def GetCurso(self):
        return self.__curso

    def SetCurso(self, curso):
        self.__curso = curso 

    def GetAsignatura (self):
        return self.__asignatura

    def SetAsignatura(self, asignatura):
        self.__asignatura = asignatura    

    def MostrarAlumno(self):
       print("Alumno")
       print("\tNombre:",self.GetNombre())
       print("\tApellidos:",self.GetApellido())
       print("\tEdad:",self.GetEdad())
       print("\tCurso:",self.__curso)
       print("\tMatriculas:",self.__asignatura)

#Alumno 1
alumno1 = Alumno ()
alumno1.SetNombre ("Daniel")
alumno1.SetAsignatura ("Salcedo")
alumno1.SetEdad (35)
alumno1.SetCurso ("Bachillerato")
alumno1.SetAsignatura(["Matemáticas", "Inglés", "Física"])
alumno1.MostrarAlumno()

#Alumno 2
alumno2 = Alumno ()
alumno2.SetNombre ("José")
alumno2.SetAsignatura ("Díaz")
alumno2.SetEdad (32)
alumno2.SetCurso ("Bachillerato")
alumno2.SetAsignatura(["Matemáticas", "Inglés", "Quimica"])
alumno2.MostrarAlumno()



  









