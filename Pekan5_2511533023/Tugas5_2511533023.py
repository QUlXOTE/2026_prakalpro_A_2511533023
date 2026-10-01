n_3023 = int(input("masukkan angka: "))
print("#", end="")
for i_3023 in range(4 * n_3023 + 5):
    print("=", end="")
print("#", end="")
print()

for baris_3023 in range(n_3023, 0, -1):
        print("| ", end="")
        for spsi_3023 in range(2 * (n_3023 - baris_3023)):
            print(" ", end="")
        for angka_3023 in range(baris_3023, 0, -1):
            print(str(angka_3023) + " ", end="")
        print("<*>", end="")
        for angka_3023 in range(1, baris_3023 + 1):
            print(" " + str(angka_3023), end="")
        for spasi_3023 in range(2 * (n_3023 - baris_3023)):
            print(" ", end="")
        print(" |", end="")
        print()

print("|", end="")
for spasi_3023 in range(2 * n_3023 + 1):
    print(" ", end="")
print("<*>", end="")
for spasi_3023 in range(2 * n_3023 + 1):
    print(" ", end="")
print("|", end="")
print()

for baris_3023 in range(1, n_3023 + 1):
        print("| ", end="")
        for spsi_3023 in range(2 * (n_3023 - baris_3023)):
            print(" ", end="")
        for angka_3023 in range(baris_3023, 0, -1):
            print(str(angka_3023) + " ", end="")
        print("<*>", end="")
        for angka_3023 in range(1, baris_3023 + 1):
            print(" " + str(angka_3023), end="")
        for spasi_3023 in range(2 * (n_3023 - baris_3023)):
            print(" ", end="")
        print(" |", end="")
        print()

print("#", end="")
for i_3023 in range(4 * n_3023 + 5):
    print("=", end="")
print("#", end="")
print()
