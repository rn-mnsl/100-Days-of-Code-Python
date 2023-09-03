# Conditional Statement 

# if condition;
#     do this
# else: 
#     do this

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# bill = 0 
# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age?"))
#     if age < 12:
#       print("Child tickets $5.")
#       bill = 5

#     elif age <= 18:
#       print("Youth tickets $7.")
#       bill = 7
    
#     elif age >= 45 and age <= 55:
#       print("Everything is going to be ok. Have a free ride!")
#     else: 
#       print("Adult tickets $12.")
#       bill = 12
    
    

#     wants_photo = input("Do you want a photo taken? Y or N. ")
#     if wants_photo == "Y":
#        bill += 3
    
#     print(f"Your final bill is ${bill}")

# else: 
#     print("Sorry, you have to grow taller before you can ride.")


# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))

# BMI = round(weight / height ** 2)

# if BMI < 18.5: 
#     print(f"Your BMI is {BMI}, you are underweight.")
# elif BMI < 25:
#     print(f"Your BMI is {BMI}, you have a normal weight.")
# elif BMI < 30: 
#     print(f"Your BMI is {BMI}, you are slightly overweight.")
# elif BMI < 35: 
#     print(f"Your BMI is {BMI}, you are obese.")
# else: 
#     print(f"Your BMI is {BMI}, you are clinically obese.")

# #PIZZA DELIVERY

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# bill = 0 

# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20 
# else: 
#     bill += 25

# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else: 
#         bill += 3
        
# if extra_cheese == "Y":
#     bill += 1

# print(f"Your final bill is: ${bill}.")

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lover1 = name1.lower()
lover2 = name2.lower()

first_digit = lover1.count("t") + lover1.count("r") + lover1.count("u") + lover1.count("e")
second_digit = lover1.count("l") + lover1.count("o") + lover1.count("v") + lover1.count("e")

print(first_digit)
print(second_digit)