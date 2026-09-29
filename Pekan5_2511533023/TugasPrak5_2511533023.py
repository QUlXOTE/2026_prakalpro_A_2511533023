tinggi_3023 = int(input("Masukkan pola: "))

for i_3023 in range(1, tinggi_3023 + 1):
    for j_3023 in range(tinggi_3023 - i_3023):
        print(" ", end="")
    for k_3023 in range(2 * i_3023 - 1):
        print("*", end="")
    print()