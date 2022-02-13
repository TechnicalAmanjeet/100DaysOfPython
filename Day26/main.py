# ********** List comprehension challenge **********

# challange 1.
string = "Amanjeet"
new_list = [alphabet for alphabet in string]
# print(len(new_list))

#challange 2
new_list = [number * 2 for number in range(0, 11)]
# print(new_list)

# challenge 3.
names = ["Amanjeet", "Kajal", "Riya", "Neha", "abp", "kismat", "Anjali", "a", "b"]

new_names_list = [name.upper() for name in names if len(name) > 3]
# print(new_names_list)


# ******** Dict comprehension challenge *********