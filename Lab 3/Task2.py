# FUNCTION TO CONVERT TO F:
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

# FUNCTION TO CONVERT TO C:
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

# UI:
def header():
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")

def footer():
    print("\nExiting program... Goodbye!")

# MAIN CODE:
while True:
    header()
    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            try:
                c = float(input("Enter temperature in Celsius: "))
                f = celsius_to_fahrenheit(c)
                print(f"{c}°C is {f:.0f}°F")
            except ValueError:
                print("Invalid input! Please enter a numeric temperature.")

        elif choice == 2:
            try:
                f = float(input("Enter temperature in Fahrenheit: "))
                c = fahrenheit_to_celsius(f)
                print(f"{f}°F is {c:.0f}°C")
            except ValueError:
                print("Invalid input! Please enter a numeric temperature.")

        elif choice == 3:
            footer()
            break

        else:
            print("Invalid choice! Please select 1, 2 or 3.")

    except ValueError:
        print("Invalid input! Choice must be a number.")