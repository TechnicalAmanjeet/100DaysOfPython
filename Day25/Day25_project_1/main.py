import pandas as pd

csv_data = pd.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(csv_data.shape) # get the shape of csv data

# find the value of all the gray , red and black people in the data.
all_coloured_people = csv_data["Primary Fur Color"]

gray_colored_people = csv_data[all_coloured_people == "Gray"]
black_colored_people = csv_data[all_coloured_people == "Black"]
red_colored_people = csv_data[all_coloured_people == "Cinnamon"]

far_color_data_dict = {"Fur Color": ["Gray", "Black", "Red"],
                       "Count": [len(gray_colored_people), len(black_colored_people), len(red_colored_people)]}

# print(far_color_data_dict)

far_color_datafram = pd.DataFrame(data=far_color_data_dict)
print(far_color_datafram)

far_color_datafram.to_csv("far_color.csv")

# print(len(black_colored_people))
# print(len(all_coloured_people))
# print(len(red_colored_people))