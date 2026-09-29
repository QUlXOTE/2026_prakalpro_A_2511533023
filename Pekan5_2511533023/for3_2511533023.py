ulang_3023 = int(input("Masukkan jumlah perulangan: "))
jumlah_3023 = 0
for i in range(1, ulang_3023 + 1):
    print(i, end=" ")
    jumlah_3023 = jumlah_3023 + i

    if i < ulang_3023:
        print(" + ", end="")
    else:
        print(" = ", jumlah_3023, end="")
print()
print("jumlah = ", jumlah_3023)
