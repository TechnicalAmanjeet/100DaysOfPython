# idea : take input from user whether user wants to perform decoding and encoding.
# then in both operation ask user to shift number.
#

print('''
 dP""b8    db    888888 .dP"Y8    db    88""Yb 
dP   `"   dPYb   88__   `Ybo."   dPYb   88__dP 
Yb       dP__Yb  88""   o.`Y8b  dP__Yb  88"Yb  
 YboodP dP""""Yb 888888 8bodP' dP""""Yb 88  Yb ''')

print('''
 dP""b8 88 88""Yb 88  88 888888 88""Yb 
dP   `" 88 88__dP 88  88 88__   88__dP 
Yb      88 88"""  888888 88""   88"Yb  
 YboodP 88 88     88  88 888888 88  Yb ''')

print('''
 dP""b8    db    8b    d8 888888 
dP   `"   dPYb   88b  d88 88__   
Yb  "88  dP__Yb  88YbdP88 88""   
 YboodP dP""""Yb 88 YY 88 888888 ''')



while True:
    user_input = input("\nType 'encode' to encrypt and Type 'decode' to decrypt : ")
    if user_input == 'encode':
        user_msg = input("Enter your massage to encrypt : ").lower()
        shift_number = int(input("Enter shift Number : "))
        encrypt_msg = ""
        element_number = 0  # char value for each element after shift
        for element in user_msg:
            element_number = ord(element) + shift_number%26
            if element_number > ord('z'):
                element_number = ord('a') + (element_number - ord('z') - 1)
            encrypt_msg += chr(element_number)

        print(f"Your encrypted msg : {encrypt_msg}")


    elif user_input == 'decode':
        user_msg = input("Enter your massage to decrypt : ").lower()
        shift_number = int(input("Enter shift Number : "))
        decrypt_msg = ""
        element_number = 0  # char value for each element after shift
        for element in user_msg:
            element_number = ord(element) - shift_number%26
            if element_number < ord('a'):
                element_number = ord('z') - (ord('a') - element_number) + 1
            decrypt_msg += chr(element_number)

        print(f"Your encrypted msg : {decrypt_msg}")



    else:
        print("Please read instruction properly and then type your input correctly.")

    game_start_or_end = input("Type 'yes' to play again or Type 'no' to exit : ")
    if game_start_or_end == 'no':
        break


print("""
.-. . . .-. . . . .   . . .-. . .   .-. .-. .-.   .-. .   .-. . . .-. . . .-.   .-. . . .-. .-.   .-. .-. .  . .-. 
 |  |-| |-| |\| |<     |  | | | |   |-  | | |(    |-' |   |-|  |   |  |\| |..    |  |-|  |  `-.   |.. |-| |\/| |-  
 '  ' ` ` ' ' ` ' `    `  `-' `-'   '   `-' ' '   '   `-' ` '  `  `-' ' ` `-'    '  ' ` `-' `-'   `-' ` ' '  ` `-' 
                                                                                                                   """)