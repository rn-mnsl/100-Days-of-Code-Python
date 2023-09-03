
# #Function with Outputs 

# def format_name(f_name, l_name):
#   formatted_f_name = f_name.title()
#   formatted_l_name = l_name.title()
#   return f"{formatted_f_name} {formatted_l_name}"

# print(format_name("RoaN", "MAnAnSalA"))

# #Function with Outputs & Multiple return 

# def format_name(f_name, l_name):
#   if f_name == "" or l_name == "":
#     return "You didn't provide valid inputs"
#     #early return statement to terminate the function 
#   formatted_f_name = f_name.title()
#   formatted_l_name = l_name.title()
#   return f"{formatted_f_name} {formatted_l_name}"

# print(format_name(input("What is your first name? "), input("What is your last name? ")))


#Calculator

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

#Add 
def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)
  num1 = float(input("What's the fist number?:" ))
  
  for symbol in operations:
    print(symbol)
  should_continue = True 
  
  while should_continue: 
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    if input(f"Type 'y' to continue with {answer}, or type 'n' to start a new calculation: ") == "y":
      num1 = answer
    else: 
      should_continue = False
      calculator()

  calculator()