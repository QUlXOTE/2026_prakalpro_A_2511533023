from typing import Final
PI_3023: Final = 3.14
print("pi: %f" % (PI_3023))
jari_3023 = float(input('Masukkan nilai jari-jari: '))
luas_3023 = PI_3023 * jari_3023 * jari_3023
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_3023, luas_3023))