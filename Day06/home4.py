# website : https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Home%204&url=worlds%2Ftutorial_en%2Fhome4.json

def one_row():
    for i in range(3):
        move()

def turn_right():
    for i in range(3):
        turn_left()

def one_fourth():
    one_row()
    turn_left()
    one_row()
    turn_right()

def complete():
    for i in range(3):
        one_fourth()
        move()
        turn_right()

complete()
one_fourth()