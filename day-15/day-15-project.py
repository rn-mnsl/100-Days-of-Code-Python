# Create a coffee machine

from data import resources
from data import MENU

# TODO Program requirements
# 1. Print report
# 2. Check resources sufficiency?
# 3. Process coins
# 4. Check transaction successful?
# 5. Make Coffee and deduct the resources

profit = 0 
def prompt():
    """Ask the user what to do """
    answer = input("What would you like? (espresso/latte/cappuccino): ")
    return answer


def report():
    """Report the current status of the coffee machine"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")

def check_resources(order_ingredients):
    """Checks if the ingredients are enough"""
    for item in order_ingredients: 
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def process_coins():
    """Returns the total amount of coins"""
    print("Please insert coins. ")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Return true when payment is enough, of false if not enough"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True 
    else: 
        print("Sorry that's not enough money. Money refunded")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} *coffee*")



is_on = True

while is_on:
  response = prompt()

  if response == 'off':
      is_on = False
  elif response == 'report':
      report()
  else:
      drink = MENU[response]
      if check_resources(drink["ingredients"]):
          payment = process_coins()
          if is_transaction_successful(payment, drink["cost"]): 
              make_coffee(response, drink["ingredients"])
              