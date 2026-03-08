password = input("Enter a password: ")

letterLower = False
letterUpper = False
numbers = False
special_char = False

if 6 <= len(password) <= 16:
    for char in password:
        if char.islower():
            letterLower = True
        elif char.isupper():
            letterUpper = True
        elif char.isdigit():
            numbers = True
        elif char in "$#@":
            special_char = True

    if letterLower and letterUpper and numbers and special_char:
        print("Valid password")
    else:
        print("Invalid password")
else:
    print("Invalid password length")