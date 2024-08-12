# Exercitiul 1

# from turtle import Turtle, Screen
# import math

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("green")
# for i in range(4):
#     timmy.forward(100)
#     timmy.right(90)
# timmy.right(0.5*90)
# timmy.forward(100*math.sqrt(2))

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# Exercitiul 2

# from prettytable import PrettyTable
# table=PrettyTable()
# table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
# table.add_column("Type",["Electric","Water","Fire"])


# print(table)

#Exercitiul 3
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker
from menu import Menu, MenuItem

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

money_machine.report()
coffee_maker.report()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "refill":
        coffee_maker.refill()
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
        