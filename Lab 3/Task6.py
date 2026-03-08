while True:
    try:
        n = int(input("How many numbers do you want to enter? "))
        if n <= 0:
            print("Please enter a positive number.")
            continue
        break
    except ValueError:
        print("Invalid input! Please enter a numeric value.")

numbers = []
for i in range(n):
    while True:
        try:
            num = int(input(f"Enter number {i+1}: "))
            numbers.append(num)
            break
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

evenCount = 0
oddCount = 0

for num in numbers:
    if num % 2 == 0:
        evenCount += 1
    else:
        oddCount += 1

print("Number of even numbers:", evenCount)
print("Number of odd numbers:", oddCount)