#Data Types 

#String 
print("Hello"[0]) #H 
print("Hello"[4]) #0

#Type Casting 
new_num_char = str(num_char)

#Data Types
num_char = len(input("What is your name?\n"))
print("Your name has " + new_num_char + " characters")
#Error = cannot concatenate str to int

#type - check the type of data 
type(num_char)


#Type Casting 
new_num_char = str(num_char)

a = str(123)
print(type(a))

print(70 + float("100.5"))
print(str(70) + str(100))

print(3 * 3 + 3 / 3 - 3) #7
print(3 * (3 + 3) / 3 - 3) #3

print(round(8 / 3, 2))

# score = 0 

# score += 1


score = 0 
height = 1.8
isWinning = True 

#f-string 

print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")

#Day 2 Project 
print(("----Welcome the to Tip Calculator----"))
bill = float(input("Enter the total bill in pesos: P"))
num_person = int(input("Enter the number of people that will split the bill: "))
tip = float(input("Enter the percentage of the tip: ")) / 100

total_bill = bill + (bill * tip)
total_share = round(total_bill / num_person, 2)
total_share = "{:.2f}".format(total_share)
print(f"Each person will share: P{total_share}")