# deklarasi variabel boolean
is_lulus_3023 = True
is_cumlaude_3023 = True

# Menggunakan Boolean
nilai_3023 = 85
batas_lulus_3023 = 75

# Menentukan nilai Boolean berdasarkan kondisi
status_kelulusan_3023 = nilai_3023 >= batas_lulus_3023

print("=== Check Kelulusan ===")
print("Nilai:", nilai_3023)
print("Apakah Lulus:", status_kelulusan_3023)
if is_lulus_3023 and is_cumlaude_3023:
    print("Selamat, Anda Lulus dengan predikat Cum laude!")

