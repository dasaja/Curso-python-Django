from menu import Menu
from coffe_maker import CoffeMaker
from money_machine import  MoneyMachine

#crear los objetos
money_machine = MoneyMachine
coffe_maker = CoffeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"Qué te gustaría ? ({options}):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffe_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        is_enough_ingredients = coffe_maker.is_resource_sufficient(drink)
        is_paymant_successful = money_machine.make_payment(drink.cost)
        if is_enough_ingredients and is_paymant_successful:
            coffe_maker.make_coffe(drink)