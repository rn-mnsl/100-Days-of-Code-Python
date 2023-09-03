import random

Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

game_images = [Rock, Paper, Scissors]
print(game_images[user_choice])

print("Computer Chose")

computer_choice = random.randint(0, 2)
print(game_images[computer_choice])

if user_choice == 0 and computer_choice == 2: 
    print("You win")
elif user_choice == 2 and computer_choice == 0: 
    print("You lose")
elif computer_choice > user_choice: 
    print("You lose")
elif computer_choice < user_choice: 
    print("You win!")
else: 
    print("Draw")
