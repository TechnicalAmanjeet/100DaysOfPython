# method 1 to read csv file.
# with open("weather_data.csv") as file:
#     data = []
#     for line in file.readlines():
#         data.append(line.strip())
#         # print(data)
# print(data)

# method2 => By using inbuilt csv file.
import csv

# write data to csv file
# with open("weather_data1.csv", "w") as csv_file:
#     data = ["Amanjeet", 143, "Riya"]
#     csv_writer = csv.writer(csv_file)
#     csv_writer.writerow(data)

# read data from csv file.
# with open("weather_data.csv") as csv_file:
#     c = csv.reader(csv_file)
#     for data in c:
#         print(data)

# extract temp data from weather data csv file.
# with open("./weather_data.csv") as csv_file:
#     temp = []
#     day = []
#     condition = []
#     index = 0
#     csv_data = csv.reader(csv_file)
#     for row in csv_data:
#         if index == 0:
#             index_of_day = row.index("day")
#             index_of_temp = row.index("temp")
#             index_of_condition = row.index("condition")
#             # print(index_of_temp)
#             index += 1
#         else:
#             temp.append(int(row[index_of_temp]))
#             day.append(row[index_of_day])
#             condition.append(row[index_of_condition])
#     print(day, temp, condition)

# open csv file by using pandas library
import pandas as pd

temp_data = pd.read_csv("weather_data.csv")
# print(temp_data)
day = temp_data.condition
# print(day)

# extract temprature from above data file.

# # Method 1.
# temp_series = temp_data["temp"]
# # print(temp_series)
#
# # convert pandas series datatype into python list
# temp_list = temp_series.to_list()
# # print(temp_list)
#
# # find avg temp of this weak.
# avg_temp = sum(temp_list) / len(temp_list)
# print(f"Avg temp of this weak : {round(avg_temp,2)}")

# Method 2.
temp_series = temp_data["temp"]
# find mean value directly by using pandas series method.
avg_temp = temp_series.mean()
# print(f"Avg temp of this weak : {round(avg_temp, 2)}")

# find max value.
max_temp = temp_series.max()
# print(f"Max temp of this weak is : {max_temp}")

# how to find a particular row which satisfy some condition

# 1. row whos day is Monday
x = temp_data.day == "Monday"
# print(temp_data[temp_data.day == "Monday"])

# 2. row whose temp is 14
row = temp_data.temp == 14
# print(temp_data[row])

# 3. row whose condition is sunny
row_cond = temp_data.condition == "Sunny"
# print(temp_data[row_cond])

# 4. row whose temp is max among the all.
# method 1.
max_temp_data = temp_data.temp.max()
row_max_temp = temp_data.temp == max_temp_data
# print(temp_data[row_max_temp])

# method 2.
max_temp_row = temp_data[temp_data.temp == temp_data.temp.max()]
# print(max_temp_row)

# 5. row whos temp is min among the all
min_temp_row = temp_data[temp_data.temp == temp_data.temp.min()]
# print(min_temp_row)

# 6. get temp of monday and convert it to farenhite. (  celcius_temp * 9/5 + 32 = fahrenhite)
monday_temp = float(temp_data[temp_data.day == "Monday"].temp * 9 / 5 + 32)
# print(f"Monday's temp in fahrenhite : {monday_temp}")

# final challenge => make dataframe from scratch.
my_list = [
    ["Amanjeet", 21, "Salarpur"],
    ["Riya", 16, "Salarpur"],
    ["Neha", 22, "Jhajha"],
    ["Kajal", 22, "Maheshpur"],
    ["Kismat", 21, "Bhirha"]
]

# import Jinja2

# now i need to convert my list into dataframes.
my_dataframe = pd.DataFrame(data=my_list, columns=["Name", "Age", "Village"])
# print(my_dataframe)
print(type(my_dataframe))
# print(my_dataframe.values)
print(my_dataframe.at[2, "Name"])
# my_dataframe.to_csv("person.csv")