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
import openpyxl  # openpyxl must be install to work with excel file.
import lxml  # lxml module must be installed to work with html file
import html5lib # html5lib must be there to work with html5 file
# import BeautifulSoup4

# # read csv file by using pandas
# csv_file = pd.read_csv("weather_data1.csv")
# print(csv_file)
#
# # read excel file by using pandas.
# excel_file = pd.read_excel("Book1.xlsx")
# print(excel_file)

# # read html file by using pandas
# html_file = pd.read_html("index.html")
# print(html_file)

# data = ["Amanjeet", 143, "Riya"]

# work with pandas csv file.
csv_file = pd.read_csv("weather_data1.csv")
# print(type(csv_file))
# print(type(csv_file["day"]))

print(csv_file)

html_data = csv_file.to_html()
print(html_data)



