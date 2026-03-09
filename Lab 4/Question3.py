arr = []
n = int(input("Enter number of elements: "))

for i in range(n):
    arr.append(int(input("Enter element: ")))

arr.sort()
key = int(input("Enter element to search: "))

low = 0
high = len(arr) - 1
found = False

while low <= high:
    mid = (low + high) // 2
    if arr[mid] == key:
        print("Element found at index", mid)
        found = True
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print("Element not found")