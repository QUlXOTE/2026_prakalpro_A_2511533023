print("=== SISTEM TRANSAKSI TOKO ===")
print()

namaPelanggan_3023 = input("Masukkan Nama Pelanggan : ")
statusPelanggan_3023 = input("Masukkan Status Pelanggan (member/nonmember) : ").strip().lower()
totalBelanja_3023 = float(input("Masukkan Total Belanja : "))
jumlahBarang_3023 = int(input("Masukkan Jumlah Barang : "))
kodePromo_3023 = input("Masukkan Kode Promo : ").strip().upper()


daftar_promo_3023 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]

# Operator Perbandingan
minBelanjaValid_3023 = totalBelanja_3023 >= 200000
minBarangValid_3023 = jumlahBarang_3023 >= 3
isMember_3023 = statusPelanggan_3023 == "member"

# Operator Keanggotaan (Membership: in dan not in)
promoTersedia_3023 = kodePromo_3023 in daftar_promo_3023
promoTidakTersedia_3023 = kodePromo_3023 not in daftar_promo_3023

# Operator Logika (and, or, not)
dapatDiskon_3023 = isMember_3023 and minBelanjaValid_3023
dapatPromo_3023 = (minBarangValid_3023 or isMember_3023) and promoTersedia_3023
bukanNonmember_3023 = not (statusPelanggan_3023 == "nonmember")


persenDiskon_3023 = 0.10 if dapatDiskon_3023 else 0.00

# Operator Aritmatika: Perkalian (*), Pengurangan (-), Pembagian (/), Sisa Bagi (%)
besarDiskon_3023 = totalBelanja_3023 * persenDiskon_3023
totalBayar_3023 = totalBelanja_3023 - besarDiskon_3023
rataHarga_3023 = totalBelanja_3023 / jumlahBarang_3023
sisaPoin_3023 = int(totalBelanja_3023) % 1000

# Operator Penugasan (Augmented Assignment: +=, -=)
if dapatPromo_3023 and kodePromo_3023 == "HEMAT10":
    besarDiskon_3023 += 10000
    totalBayar_3023 -= 10000


list_a_3023 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]
list_b_3023 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]
list_c_3023 = list_a_3023

identitasSama_3023 = list_a_3023 is list_c_3023
identitasBeda_3023 = list_a_3023 is not list_b_3023
nilaiSama_3023 = list_a_3023 == list_b_3023


BIT_MEMBER_3023 = 0b0001
BIT_BELANJA_3023 = 0b0010
BIT_BARANG_3023 = 0b0100
BIT_PROMO_3023 = 0b1000

# Menggabungkan kondisi menggunakan Bitwise OR (|)
kodeStatus_3023 = 0
if isMember_3023:
    kodeStatus_3023 |= BIT_MEMBER_3023
if minBelanjaValid_3023:
    kodeStatus_3023 |= BIT_BELANJA_3023
if minBarangValid_3023:
    kodeStatus_3023 |= BIT_BARANG_3023
if promoTersedia_3023:
    kodeStatus_3023 |= BIT_PROMO_3023

# Pemeriksaan Kondisi menggunakan Bitwise AND (&)
cekMember_3023 = kodeStatus_3023 & BIT_MEMBER_3023
cekPromo_3023 = kodeStatus_3023 & BIT_PROMO_3023

# Perbandingan Status menggunakan Bitwise XOR (^)
kodeReferensi_3023 = 0b1011
hasilXor_3023 = kodeStatus_3023 ^ kodeReferensi_3023

# Bitwise Shift (<<)
hasilShift_3023 = kodeStatus_3023 << 1


print("=== DATA TRANSAKSI ===")
print(f"Nama Pelanggan        : {namaPelanggan_3023}")
print(f"Status Pelanggan      : {statusPelanggan_3023}")
print(f"Total Belanja         : Rp{totalBelanja_3023:.0f}")
print(f"Jumlah Barang         : {jumlahBarang_3023}")
print(f"Kode Promo            : {kodePromo_3023}")
print()

print("=== HASIL VALIDASI ===")
print(f"Belanja >= Rp200000        : {minBelanjaValid_3023}")
print(f"Jumlah Barang >= 3         : {minBarangValid_3023}")
print(f"Status Member              : {isMember_3023}")
print(f"Kode Promo Tersedia        : {promoTersedia_3023}")
print(f"Mendapatkan Diskon         : {dapatDiskon_3023}")
print(f"Mendapatkan Promo          : {dapatPromo_3023}")
print()

print("=== HASIL PERHITUNGAN ===")
print(f"Diskon                     : Rp{besarDiskon_3023:.0f}")
print(f"Total Pembayaran           : Rp{totalBayar_3023:.0f}")
print(f"Rata-rata Harga Barang     : Rp{rataHarga_3023:.2f}")
print(f"Sisa Pembagian Belanja (%) : {sisaPoin_3023}")
print()

print("=== HAK AKSES PELANGGAN ===")
print(f"Kode Hak Akses             : {bin(kodeStatus_3023)[2:].zfill(4)}")
print(f"Member Access              : {cekMember_3023 > 0}")
print(f"Promo Access               : {cekPromo_3023 > 0}")
print(f"Free Shipping Access       : {kodePromo_3023 == 'GRATISONGKIR'}")
print()

print("=== DEMONSTRASI OPERATOR IDENTITAS ===")
print(f"list_a is list_c           : {identitasSama_3023} (Objek sama di memori)")
print(f"list_a is not list_b       : {identitasBeda_3023} (Objek beda tempat memori)")
print(f"list_a == list_b          : {nilaiSama_3023} (Nilai isi list sama)")
print()

print("=== OPERASI BITWISE ===")
print("=== Kode Status Transaksi ===")
print("0001 | 0010 | 0100 | 1000")
print(f"Kode Biner    : {bin(kodeStatus_3023)[2:].zfill(4)}")
print(f"Kode Desimal  : {kodeStatus_3023}")
print()

print("=== Pemeriksaan Status ===")
print("Cek Member")
print(f"{bin(kodeStatus_3023)[2:].zfill(4)} & 0001")
print(f"Hasil Biner   : {bin(cekMember_3023)[2:].zfill(4)}")
print(f"Hasil Desimal : {cekMember_3023}")
print()

print("Cek Promo")
print(f"{bin(kodeStatus_3023)[2:].zfill(4)} & 1000")
print(f"Hasil Biner   : {bin(cekPromo_3023)[2:].zfill(4)}")
print(f"Hasil Desimal : {cekPromo_3023}")
print()

print("=== Perbandingan Status ===")
print(f"Kode Transaksi : {bin(kodeStatus_3023)[2:].zfill(4)}")
print(f"Kode Referensi : {bin(kodeReferensi_3023)[2:].zfill(4)}")
print(f"{bin(kodeStatus_3023)[2:].zfill(4)} ^ {bin(kodeReferensi_3023)[2:].zfill(4)}")
print(f"Hasil Biner   : {bin(hasilXor_3023)[2:].zfill(4)}")
print(f"Hasil Desimal : {hasilXor_3023}")
print()

print("=== Shift ===")
print(f"{bin(kodeStatus_3023)[2:].zfill(4)} << 1")
print(f"Hasil Biner   : {bin(hasilShift_3023)[2:].zfill(5)}")
print(f"Hasil Desimal : {hasilShift_3023}")
print()

print("=== SELESAI ===")