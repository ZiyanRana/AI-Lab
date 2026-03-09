queue = []

while True:
    print("1.Enqueue 2.Dequeue 3.Display 4.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        item = input("Enter element: ")
        queue.append(item)
    elif choice == 2:
        if len(queue) == 0:
            print("Queue is empty")
        else:
            print("Dequeued element:", queue.pop(0))
    elif choice == 3:
        print("Queue:", queue)
    elif choice == 4:
        break