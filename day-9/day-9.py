programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again.",
  "Loop:": "Another entry"
}

#Retrieving items from dictionary
print(programming_dictionary["Function"])

#Adding items to dictionary. 
programming_dictionary["Loop"] = "The action of doing over and over again"

#Create an empty dictionary 
empty_dictionary = {}

#Wipe an existing dictionary 
programming_dictionary = {}

#Edit an item in a dictionary 
programming_dictionary["Bug"] = "A moth in your computer"

#Loop through a dictionary 
for thing in programming_dictionary: 
  print(thing)
  print(programming_dictionary[thing])


#Nesting 
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

#Nesting a List in a Dictionary

travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting Dictionary in a Dictionary

travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

#Nesting Dictionaries in Lists

travel_log = [
{
  "country": "France", 
  "cities_visited": ["Paris", "Lille", "Dijon"], 
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]


bids = {}
should_continue = True

print('''

  /$$$$$$                                            /$$            /$$$$$$                        /$$     /$$                    
 /$$__  $$                                          | $$           /$$__  $$                      | $$    |__/                    
| $$  \__/  /$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$  /$$$$$$        | $$  \ $$ /$$   /$$  /$$$$$$$ /$$$$$$   /$$  /$$$$$$  /$$$$$$$ 
|  $$$$$$  /$$__  $$ /$$_____/ /$$__  $$ /$$__  $$|_  $$_/        | $$$$$$$$| $$  | $$ /$$_____/|_  $$_/  | $$ /$$__  $$| $$__  $$
 \____  $$| $$$$$$$$| $$      | $$  \__/| $$$$$$$$  | $$          | $$__  $$| $$  | $$| $$        | $$    | $$| $$  \ $$| $$  \ $$
 /$$  \ $$| $$_____/| $$      | $$      | $$_____/  | $$ /$$      | $$  | $$| $$  | $$| $$        | $$ /$$| $$| $$  | $$| $$  | $$
|  $$$$$$/|  $$$$$$$|  $$$$$$$| $$      |  $$$$$$$  |  $$$$/      | $$  | $$|  $$$$$$/|  $$$$$$$  |  $$$$/| $$|  $$$$$$/| $$  | $$
 \______/  \_______/ \_______/|__/       \_______/   \___/        |__/  |__/ \______/  \_______/   \___/  |__/ \______/ |__/  |__/
''')

def find_highest_bidder(bidding_record):
  highest_bid = 0 
  winner = "" 
  for bidder in bidding_record: 
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while should_continue: 
  name = input("What is your name: \n")
  bid = int(input("What is your bid?\n"))
  bids[name] = bid
  choice = input("Are there any other bidders? Type 'yes' or 'no'\n")
  
  if choice == "no":
    should_continue = False
    find_highest_bidder(bids)
    