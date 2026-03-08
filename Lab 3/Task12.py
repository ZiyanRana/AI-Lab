data = input("Enter comma-separated 4-digit binary numbers: ")

binaries = data.split(",")
result = []

for b in binaries:
    decimal = int(b, 2)  
    if decimal % 5 == 0: 
        result.append(b)

print("Numbers divisible by 5:", ",".join(result))