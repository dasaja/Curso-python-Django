class CoffeMaker:
    """Modelo de la máquina que hace el café"""

    def __int__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffe": 100,
        }

    def report(self):
        """Imprime un informe de todos los recursos de la máquina de café"""
        print(f"Agua: {self.resources['water']}ml")
        print(f"Leche: {self.resources['milk']}ml")
        print(f"Cafe: {self.resources['coffe']}g")

    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffe": 100,
        }

    def report(self):
        """Imprime un informe de todos los recursos de la maquina de cafe"""
        print(f"Agua: {self.resources['water']}ml")
        print(f"Leche: {self.resources['milk']}ml")
        print(f"Cafe: {self.resources['coffe']}g")




    def is_resource_sufficient(self, drink):
        """Devuelve True cuando se puede hacer el pedido,Falso si los ingredientes son insuficientes"""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Lo siento, no hay suficiente {item}.")
                can_make = False
        return can_make
    def make_coffe(self, order):
        """Deduce los ingredientes necesarios de los recursos"""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Aqui esta tu {order.name} ☕️. disfrutalo!")


