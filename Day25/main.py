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
with open("./weather_data.csv") as csv_file:
    temp = []
    day = []
    condition = []
    index = 0
    csv_data = csv.reader(csv_file)
    for row in csv_data:
        if index == 0:
            index_of_day = row.index("day")
            index_of_temp = row.index("temp")
            index_of_condition = row.index("condition")
            # print(index_of_temp)
            index += 1
        else:
            temp.append(int(row[index_of_temp]))
            day.append(row[index_of_day])
            condition.append(row[index_of_condition])
    print(day, temp, condition)

