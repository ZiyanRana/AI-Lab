lines = []

print("Enter lines of text (press Enter on a blank line to finish):")
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

print("\nLines in lowercase:")
for line in lines:
    print(line.lower())