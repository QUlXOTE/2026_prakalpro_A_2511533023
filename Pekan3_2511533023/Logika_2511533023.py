a1_3023 = input("input nilai boolean-1 (true/false): ").strip().lower() == "true"
a2_3023 = input("input nilai boolean-2 (true/false): ").strip().lower() == "true"

print("\nA1 =", a1_3023)
print("A2 =", a2_3023)

#konjungasi: bernilai True jika keduanya True
hasil_3023 = a1_3023 and a2_3023
print("\nOperator Konjungsi (AND)")
print("A1 and A2 =", hasil_3023)

# Disjungsi: bernilai True jika salah satu True
hasil_3023 = a1_3023 or a2_3023
print("\nOperator Disjungsi (OR)")
print("A1 or A2 =", hasil_3023)

#negasi: membalik nilai A1
hasil_3023 = not a1_3023
print("\nNegasi (NOT)")
print("not A1 =", hasil_3023)

# Negaasi: A2 membalik nilai A2
hasil_3023 = not a2_3023
print("\nNegasi (NOT)")
print("not A2 =", hasil_3023)

# XOR: beranilai true jika kedua nilai berbeda
hasil_3023 = a1_3023 ^ a2_3023
print("\nDisjungsi Eksklusif (XOR)")
print("A1 XOR A2 =", hasil_3023)