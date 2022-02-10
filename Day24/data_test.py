with open("data.txt", 'w') as file:
    data = "10"
    file.write(data)

with open("data.txt") as file:
    content = file.read()
    print(content)
    print(type(content))