#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# ******** started working on this project from here ***********
INVITED_NAME_PATH = "./Input/Names/invited_names.txt"
DESTINATION_FILE_PATH = "./Output/ReadyToSend/"
STARTING_FILE_PATH = "./Input/Letters/starting_letter.txt"

def create_file(name, data):
    file_name = f"letter_for_{name[0:-1]}.txt"
    file_path = DESTINATION_FILE_PATH + file_name
    # print(file_path)
    with open(file_path, "w") as file:
        file.write(data)

first_line_of_letter = ""
rest_line_of_letter = ""
i = 0

with open(STARTING_FILE_PATH) as starting_file:
    for line in starting_file.readlines():
        if i == 0:
            first_line_of_letter += line[0:5]
            i += 1
        else:
            rest_line_of_letter += line

# print(rest_line_of_letter


def create_data(name):
    data = first_line_of_letter + name[:-1] + ",\n" + rest_line_of_letter
    return data


with open(INVITED_NAME_PATH) as invited_name_file:
    for name in invited_name_file.readlines():
        data = create_data(name)
        create_file(name, data)