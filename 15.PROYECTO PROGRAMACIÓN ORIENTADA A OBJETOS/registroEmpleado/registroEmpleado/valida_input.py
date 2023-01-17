class validar:
    def __init__(self):
        pass


    def input_valid_int(self, msg, start= 0, end= None):
        inp = input(msg)

        if not inp.isdecimal():
            print("Entrada invalida. !Intenta otra vez¡")
        elif start is not None and end is not None:
            if not(start <= int(inp) <= end):
                print("Entrada invalida. !Intenta otra vez¡")
            else:
                return int(inp)
        else:
            return int(inp)



