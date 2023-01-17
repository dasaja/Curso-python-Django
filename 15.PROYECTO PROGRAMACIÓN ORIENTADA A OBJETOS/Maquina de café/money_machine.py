class MoneyMachine:
    CURRENCY = "$"

    COIN_VALUES = {
        "25 centavos": 0.25,
        "10 centavos": 0.25,
        "5 centavos": 0.05,
        "1 centavos": 0.01,
    }

    def __int__(self):
        self.profit = 0
        self.money_recived = 0

    def report(self):
        """Imprime el beneficio actual"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Devuelve el total calculando a partir de las monedas insertadas"""
        print("Por favor inserte las monedas")
        for coin in self.COIN_VALUES:
            self.money_recived += int(input(f"Cuantas {coin}?: "))
        return  self.money_recived

    def make_payment(self, cost):
        """Devuelve True cuando se acpeta el pago  o False cuando el saldo es insuficiente"""
        self.process_coins()
        if self.money_recived >= cost:
            change = round( self.money_recived - cost, 2)
            print(f"Aqui  esta {self.CURRENCY}{change}")
            self.profit += cost
            self.money_recived = 0
            return  True
        else:
            print("Lo siento, no es suficiente dinero")
            self.money_recived = 0
            return  False
