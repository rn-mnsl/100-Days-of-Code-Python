
#Error 1: Two equal sign is needed for assignment 
number = int(input("Which number do you want to check?"))

if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")


#Error 2: The year is not converted to int data type
year = int(input("Which year do you want to check?"))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")

#Error 3: elif, 'and', [number]
for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0: 
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")  
  elif number % 5 == 0:  
    print("Buzz")
  else:
    print(number)