from art import logo, vs
from game_data import data
import random

#Display logo
print(logo)

#Create a function higher_lower
def higher_lower():
  """plays the game of higher lower"""

  #generate two random account from the gamte data
  data_1 = random.choice(data)
  data_2 = random.choice(data)
  if data_1 == data_2: 
    data_2 = random.choice(data)
  
  is_game_over = False
  current_score = 0
  
  while not is_game_over: 

    #display the two data 
    #there is an alternative way of doing this by creating a function on formatting the data 
    print(f"Compare A: {data_1['name']}, a {data_1['description']}, from {data_1['country']}")
    print(vs)
    print(f"Against B: {data_2['name']}, a {data_2['description']}, from {data_2['country']}")

    #Ask the user for a guess
    answer = input("Who has more followers, 'A' or 'B': ").lower()
    
    #Compare the two data using a check variable 
    check = ''
    if data_1['follower_count'] > data_2['follower_count']:
      check = 'a'
    elif data_1['follower_count'] < data_2['follower_count']:
      check = 'b'

    #Check is the answer of the player is right or wrong 
    if answer == check: 
      current_score += 1
      print(f"\n\n\n\n\n\n\nYou are right! Current Score: {current_score}")

      #If right, display the second one, as the first one in the two displays, then generate another random one 
      data_1 = data_2 
      data_2 = random.choice(data)
    else: 
      #Else end the game and tally the score
      print(f"Sorry, you are wrong. Final Score: {current_score}")
      is_game_over = True

higher_lower()