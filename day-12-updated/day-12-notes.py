################# Scope #####################

enemies = 1 

def increase_enemies():
  enemies = 2 
  print(f"enemies inside the function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

#Local Scope 

def drink_potion(): 
  potion_strength = 2 
  print(potion_strength)

drink_potion()
print(potion_strength)

#Global Scope

player_health = 10 

def drink_potion():
  potion_strength = 2 
  print(player_health)

drink_potion()

#When creating a variable or a function, you have to be aware on where you place it. 

# There is no Block Scope 

game_level = 3 
enemies = ["Skeleton", "Zombie", "Alien"]
if game_level < 5: 
  new_enemy = enemies[0]

# Modifying Global Scope 

def increase_enemies():
  global enemies 
  enemies += 1 

def increase_enemies():
  return enemies + 1 

enemies = increase_enemies()

