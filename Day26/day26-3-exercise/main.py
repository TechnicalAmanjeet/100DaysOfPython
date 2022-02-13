import pandas as pd

file1 = []
file2 = []

with open("file1.txt") as file1_data:
    for digit in file1_data.readlines():
        file1.append(int(digit))

with open("file2.txt") as file2_data:
    for digit in file2_data.readlines():
        file2.append(int(digit))

result = [digit for digit in file1 if digit in file2]

print(file1)
print(file2)

# Write your code above 👆

print(result)


