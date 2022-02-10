# # worst way to work with file.
#
# file = open("file.txt")
# content = file.read()
# print(content)
#
#

# Best way to work with file.
with open("file.txt", 'w') as file: # first it creates a file with file.txt filename if it does not exist.
    # print(file.read())
    data = "hii Guy's, I'm Amanjeet Kumar."
    file.write(data)

with open("file.txt") as file:
    contents = file.read()
    print(contents)

with open("file.txt", 'a') as file: # append data into the file.
    data = "\nI born and brought up in Bihar."
    file.write(data)

print("\nAfter appending the data : \n")

with open("file.txt") as file:
    contents = file.read()
    print(contents)

