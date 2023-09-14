print("Hello world!")
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')") #quote-sensitive

#String Concatenate 
print("Hello" + " " + "Angela") 

#Input Function 
print("Hello " + input("What is your name?") + "!")

#Len - count the number of variables
print( len( input("What is your name?")))

#Switcheroo
a = 5
b = 3

temp = a 
a = b 
b = temp

print(f"{a} and {b} and temp")

#Band Name generator 
print("Hello! Welcome to Band Generator.")
city = input("Which city did you grow up in?\n")
pet = input("What is the name of your pet?\n")
band_name = city + " " + pet
print(band_name)

