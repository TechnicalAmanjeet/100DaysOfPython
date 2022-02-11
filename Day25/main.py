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
print(f"Avg temp of this weak : {round(avg_temp, 2)}")
