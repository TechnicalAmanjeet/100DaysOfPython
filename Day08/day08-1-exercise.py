#Write your code below this line 👇

def paint_calc(height,width,cover):
  paint_can = (height * width)
  if paint_can % cover == 0:
    paint_can = paint_can / cover
  else:
    paint_can //= cover
    paint_can +=1


  print(f"You'll need {int(paint_can)} cans of paint.")





#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


