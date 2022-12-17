#composion => consiste crear nuevas clases a partir de otras clases ya existentes y actuan como elemtos compositores de la nueva, clases existentes seran utilizados atributos a la  nueva clase.
class Cordenada:
  def __init__(self, x, y):
    self.X = x
    self.Y = y

  def MostrarCordenada(self):
    print("(",self.X,",",self.Y,")")

class Cuadrado:
  def __init__(self, v1, v2, v3, v4):
    self.V1 = v1
    self.V2 = v2
    self.V3 = v3
    self.V4 = v4

  def MostrarVertices(self):
    print("El cuadrado esta compuesto por los siguientes vertices:")
    self.V1.MostrarCordenada()
    self.V2.MostrarCordenada()
    self.V3.MostrarCordenada()
    self.V4.MostrarCordenada()

v1 = Cordenada(1,1)
v2 = Cordenada(4,1)
v3 = Cordenada(4,4)
v4 = Cordenada(1,4)

cuadrado = Cuadrado(v1,v2,v3,v4)
cuadrado.MostrarVertices()    


