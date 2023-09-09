class User: 
  
  def __init__(self, user_id, username):
    self.id = user_id
    self.username = username
    self.followers = 0 
    self.following = 0
  
  def follow(self, user):
    user.followers += 1 
    self.following += 1 

user_1 = User("001", "roan")
user_2 = User("002", "dani")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

# Pascal Case - First Letter Capitalize
# Camel Case - first Letter, Lowercase, all Capitalize 
# snake_case - all lowercase
 
#Constructor
# class Car: 
# 	def __init__(self): 
# 	#initilize attributes

# Attribute - something that the object will have 
# class Car: 
#   def __init__(self, seats):
#     self.seats = seats 

# When you add a parameter into the constructor, it must provide that many pieces of data
# Sometimes we want a default value, we do initilizing the value directly 

# ADDING METHODS TO A CLASS
# class Car:  
#   def enter_race_mode():
#   self.seats = 2
# 
# my_car.enter_race_mode