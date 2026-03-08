def footer():
    print("\nExiting password program. Goodbye!")

# MAIN CODE:
while True:
    password = input("Enter a password (or 0 to exit): ")
    
    if password == "0":
        footer()
        break

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
            print("The password is VALID!")
            break
        else:
            if not letterLower:
                print("Invalid password, there is NO lowercase letter [a-z].")
            elif not letterUpper:
                print("Invalid password, there is NO uppercase letter [A-Z].")
            elif not number:
                print("Invalid password, there is NO number [0-9].")
            elif not specialChar:
                print("Invalid password, there is NO special character [$#@].")
    else:
        print("Invalid password length! Must be 6 to 16 characters.")