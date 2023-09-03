#Number Guessing Game

from art import logo 
import random 

EASY_LEVEL_TURNS = 10 
HARD_LEVEL_TURNS = 5

turns = 0 

def set_difficulty():
  """ set the difficulty of the game"""
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard':" )
  if difficulty == 'easy':
    return EASY_LEVEL_TURNS
  elif difficulty == 'hard':
    return HARD_LEVEL_TURNS

def check_answer(number_guess, the_number, turns):
  """check the guess against the answer. Returns the number of turns remaining."""
  if number_guess > the_number: 
    print("You're number is too high.")
    return turns - 1
  elif number_guess < the_number: 
    print("You're number is too low.")
    return turns - 1
  elif number_guess == the_number:
    print(f"You got it! The answer is {the_number} (≧▽≦)" )

def main_game():
  print(logo)
  
  print("I'm thinking of a number between 1 and 100")
  answer = random.randint(1, 100)
  turns = set_difficulty()

  guess = 0
  while answer != guess:
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = int(input("Guess the number: "))
    turns = check_answer(guess, answer, turns)
    if turns == 0: 
      print(f"You've run out of guesses. The correct answer is {answer}")
      print(f"You Lose. ╥﹏╥")
      return

main_game()
