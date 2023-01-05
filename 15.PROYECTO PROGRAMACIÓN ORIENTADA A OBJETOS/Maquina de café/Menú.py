class MenuItem:
    """Modelos para tomar del Menú Item"""
    def __int__(self, name, water, milk, coffe, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {"water": water, "milk": milk, "coffe": coffe}

class Menu:
    """Modelo con el menu de bebidas"""
    def __int__(self):
        self.menu = [MenuItem(name="late", water=200, milk=150, coffe=24, cost=2.50), MenuItem(name="espresso", water=50, milk=18,coffe=18, cost=1.50), MenuItem(name="capuccino", water=250, milk=50, coffe=24, cost=2.50)]

    def get_items(self):
        """Retorna todos los items del menu"""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
            print(options)
        return print(options)
    def find_drink(self, order_name):
        """Busca en el menú una bebida en particular por nombre"""
        for item in self.menu:
            if item.name == order_name:
                return item

"""
class MenuItem:
    """Modelos para coger del Menu Item."""
    def __init__(self, name, water, milk, coffe, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffe": coffe
        }
class Menu:
    """Modelo con el menu de bebidas"""
    def __init__(self):
        self.menu = [
            MenuItem(name="late", water=200, milk=150, coffe=24, cost=2.50),
            MenuItem(name="espresso", water=50, milk=18, coffe=18, cost=1.50),
            MenuItem(name="cappuccino", water=250, milk=50, coffe=24, cost=3.00)
        ]  
        
    def get_items(self):
        """Retorna todos los items del menu"""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options
def find_drink(self, order_name):
        """Busca en el menu una bebida en particular por nombre"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Lo sentimos, esa bebida no esta disponible.")          
"""



