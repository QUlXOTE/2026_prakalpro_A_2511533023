batas_3023 = int(input("Masukkan nilai batas: "))
for line_3023 in range(1, batas_3023 + 1):
    for j in range(1, (-1 * line_3023 + batas_3023) + 1):
        print(".", end="")
    print(line_3023)