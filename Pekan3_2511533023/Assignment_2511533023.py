angka1_3023 = int(input("input angka-1: "))
angka2_3023 = int(input("input angka-2: "))

print("\nNilai awal angka1 =", angka1_3023)
print("Nilai awal angka2 =", angka2_3023)

# assignment biasa 
hasil_3023 = angka1_3023
print("\nAssignment biasa (=)")
print("hasil = ", hasil_3023)

# assignment penambahan
hasil_3023 = angka1_3023
hasil_3023 += angka2_3023
print("\nAssignment penambahan (+=)")
print("hasil = ", hasil_3023)

# assignment pengurangan
hasil_3023 = angka1_3023
hasil_3023 -= angka2_3023
print("\nAssignment pengurangan (-=)")
print("hasil = ", hasil_3023)

# assignment perkalian
hasil_3023 = angka1_3023
hasil_3023 *= angka2_3023
print("\nAssignment perkalian (*=)")
print("hasil = ", hasil_3023)

# assignment pembagian, pembagian bulat, dan sisa bagi
if angka2_3023 != 0:
    hasil_3023 = angka1_3023
    hasil_3023 /= angka2_3023
    print("\nAssignment pembagian (/=)")
    print("hasil = ", hasil_3023)
    # assignment pembagian bulat
    hasil_3023 = angka1_3023
    hasil_3023 //= angka2_3023
    print("\nAssignment pembagian bulat (//=)")
    print("hasil = ", hasil_3023)

    hasil_3023 = angka1_3023
    hasil_3023 %= angka2_3023
    print("\nAssignment sisa bagi (%=)")   
    print("hasil = ", hasil_3023)
else:
    print("\nPembagian tidak dapat dilakukan.")
    print("Angaka kedua tidak boleh bernilai 0.")

# assignment perpangkat
hasil_3023 = angka1_3023
hasil_3023 **= angka2_3023
print("\nAssignment perpangkat (**=)")
print("hasil = ", hasil_3023)