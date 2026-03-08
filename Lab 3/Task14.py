password = input("Enter a password: ")

letterLower = False
letterUpper = False
number = False
specialChar = False

if 6 <= len(password) <= 16:
    for char in password:
        if char.islower():
            letterLower = True
        elif char.isupper():
            letterUpper = True
        elif char.isdigit():
            number = True
        elif char in "$#@":
            specialChar = True

    if letterLower and letterUpper and number and specialChar:
        print("Valid password")
    else:
        print("Invalid password")
else:
    print("Invalid password length")