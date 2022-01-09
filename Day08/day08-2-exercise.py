#Write your code below this line 👇

def prime_checker(number):
    n=number
    if n == 2:
        print("It's a prime number.")
        return
    for i in range(2,(n//2)+1):
        if n%i == 0:
            print("It's not a prime number.")
            return
    print("It's a prime number.")


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



