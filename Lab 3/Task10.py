m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

array = []

for i in range(m):
    row = []
    for j in range(n):
        row.append(i * j)
    array.append(row)

print("Generated 2D array:")
print(array)