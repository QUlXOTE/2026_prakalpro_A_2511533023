print("=================================")
print("1. OPERATOR KEANGGOTAAN")
print("=================================")

input_data_3023 = input("masukkan beberapa angka, pisahkan dengan koma: ")
data_3023 = [int(angka.strip()) for angka in input_data_3023.split(",")]

nilai_dicari_3023 = int(input("masukkan angka yang ingin dicari: "))

#operator in
hasil_3023 = nilai_dicari_3023 in data_3023
print("\nOperator Keanggotaan (IN)")
print(nilai_dicari_3023, "in" , data_3023, "=", hasil_3023)

# operator not in
hasil_3023 = nilai_dicari_3023 not in data_3023
print("\nOperator keanggotaan NOT IN")
print("Apakah", nilai_dicari_3023, "not in", data_3023, "=", hasil_3023)
