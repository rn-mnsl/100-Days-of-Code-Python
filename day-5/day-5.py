# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits: 
#   print(fruit)
#   print(fruit + " Pie")

# sum = 0 
# for number in range(1, 101):
#   sum += number

# print(sum)

# #FizzBuzz Exercise
# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0: 
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0: 
#         print("Buzz")
#     else:
#         print(number)

print("""
    ___    __    ______   ____  ___   ___________       ______  ____  ____     _____________   ____________  ___  __________  ____ 
   /   |  / /   / ____/  / __ \/   | / ___/ ___/ |     / / __ \/ __ \/ __ \   / ____/ ____/ | / / ____/ __ \/   |/_  __/ __ \/ __ 
  / /| | / /   / /_     / /_/ / /| | \__ \\__ \| | /| / / / / / /_/ / / / /  / / __/ __/ /  |/ / __/ / /_/ / /| | / / / / / / /_/ /
 / ___ |/ /___/ __/    / ____/ ___ |___/ /__/ /| |/ |/ / /_/ / _, _/ /_/ /  / /_/ / /___/ /|  / /___/ _, _/ ___ |/ / / /_/ / _, _/ 
/_/  |_/_____/_/      /_/   /_/  |_/____/____/ |__/|__/\____/_/ |_/_____/   \____/_____/_/ |_/_____/_/ |_/_/  |_/_/  \____/_/ |_|                                                                                                                                    
      """)

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print(">>>>Welcome to the Alf Password Generator!<<<<")
print("Here we will create a password in order to secure your accounts!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""

for letter in range(1, nr_letters + 1):
  random_char = random.choice(letters) 
  password += random_char

for symbol in range(1, nr_symbols + 1):
  random_symbol = random.choice(symbols)
  password += random_symbol

for number in range(1, nr_numbers):
  random_numbers = random.choice(numbers)
  password += random_numbers

print("Password Created Successfully!")
print(f"Your new password is: {password}")
