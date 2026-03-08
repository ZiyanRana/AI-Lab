number = 7  

while True:
    try:
        guess = int(input("Guess a number between 1 to 9: "))
        if guess < 1 or guess > 9:
            print("Please enter a number from 1-9.")
            continue

        if guess == number:
            print("Well guessed!")
            break
        else:
            print("Wrong guess, try again!")

    except ValueError:
        print("Invalid input! Please enter a numeric value.")