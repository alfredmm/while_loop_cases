def finalval():
    i = 25
    while i>12:
        print(i)
        i = i-3
    print("Final Value: ", i)

finalval()


def finalval2():
    x = 7
    while x>= 5 and x<=8:
        print(x)
        if x%2 == 0:
            x = x+1
        else:
            x = x-2
    print("Final Value: ", x)

finalval2()


def prices():
    total = 0
    
    while total<=100:
        price = int(input("Price: "))
        total = total + price
        print("Total:", total)

prices()


def valid_squareroot():
    x = int(input("Enter the number for SquareRoot:"))

    while x<0:
        print("Number cannot be negative...")
        x = int(input("Enter the number for SquareRoot:"))
    print("The squareroot of", x, "is", x**0.5)
valid_squareroot()


def password_match():
    passw = int(input("Enter the Password: "))
    correct_password = 2022

    while passw!=correct_password:
        print("Password is incorrect...")
        print()
        passw = int(input("Enter the Correct Password: "))
        print()
    print("Congratulations...Password Successful!")
password_match()

    
        
        
