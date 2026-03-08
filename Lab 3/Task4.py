for i in range(1, 10):
    if i <= 5:
        stars = i
    else:
        stars = 10 - i
    for j in range(stars):
        print("*", end="")
    print()