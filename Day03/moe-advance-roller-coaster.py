# idea implemented from this website.
# https://app.diagrams.net/?lightbox=1&target=blank&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Rollercoaster%202#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1XaUDMIKOxCUzJbsuZevgHZmgKr7rICbI%26export%3Ddownload

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

# idea : height > 120cm => can ride else can't ride
# user-age = 0;

if height > 120:
  print("You can ride! the rollercoaster")
  user_age = int(input("What is your age?"))

  # idea : user_age > 18 => pay 12 doller to ride
  # elif : user_age>=12 => pay 7 doller for (ride)
  # else pay 5 doller only for ride.
  if user_age > 18:
      print(f'You have to pay $12 to ride on rollercoaster')
  elif user_age >= 12:
      print("You hav to pay $7 to ride")
  else:
      print(f'You have to pay $5 to ride!')

else:
  print("Sorry! you have to grow taller then 120 cm before you can ride!")