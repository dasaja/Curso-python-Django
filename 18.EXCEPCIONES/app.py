class OperadorException(Exception):
    def __int__(self, mensaje):
        super().__init__(mensaje)

    def dividir(self, a, b):
        if b == 0:
            raise OperadorException("Error: No se puede dividir para cero!")
        else:
            return a / b

error = OperadorException("Error: No se puede dividir para cero!")
error.dividir(4, 0)
