stack = []

while True:
    print("1.Push 2.Pop 3.Display 4.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        item = input("Enter element: ")
        stack.append(item)
    elif choice == 2:
        if len(stack) == 0:
            print("Stack is empty")
        else:
            print("Popped element:", stack.pop())
    elif choice == 3:
        print("Stack:", stack)
    elif choice == 4:
        break