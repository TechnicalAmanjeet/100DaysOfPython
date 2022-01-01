# The idea of this game is to take two input from user
# 1st input : what's the name of city he born on?
# 2nd input : what's his pet name?

print("************ Welcome to the Band Name Generator Game *************")

# taking 1st name from user in variable : user_city_name

user_city_name = input("What is the name of city you grew up in? : ")

# taking 2nd name from user in variable : user_pet_name

user_pet_name = input("What is the name of your pet? : ")

# now print the band name for user

print(fr"Your band name could be {user_city_name} {user_pet_name}.")