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
# with open("weather_data1.csv", "a", newline='') as csv_file:
#     data = ["Amanjeet", 143, "Riya"]
#     csv_writer = csv.writer(csv_file)
#     csv_writer.writerow(data)
#
# # read data from csv file.
# with open("weather_data1.csv") as csv_file:
#     c = csv.reader(csv_file)
#     for data in c:
#         print(data)

import pandas as pd
csv_file = pd.read_csv("weather_data1.csv")
print(csv_file)