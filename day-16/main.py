from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True
while is_on:

  print(f"What would you like: {menu.get_items()}")
  order = input("Your order pls: ")
  if order == "off":
    is_on = False
  elif order == "report":
    coffee_maker.report()
  else: 
    drink = menu.find_drink(order)
    if coffee_maker.is_resource_sufficient(drink):
      if money_machine.make_payment(drink.cost):
        coffee_maker.make_coffee(drink)



