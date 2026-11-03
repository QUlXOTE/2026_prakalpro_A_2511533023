height = int(input("Enter height: "))

for row in range(height, 0, -1):
    for column in range(1, row + 1):
        if column == row:
            print("*", end="")
        else:
            print("*", end=" ")
    print()