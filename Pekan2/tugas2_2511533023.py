from typing import Final

# 1. Deklarasi Konstanta (Modul typing.Final)
BATAS_LULUS: Final[float] = 75.0

# 2. Input Data Praktikan
print("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")
nama_3023 = input("Masukkan Nama Mahasiswa : ")
jk_3023 = input("Masukkan Jenis Kelamin (L/P) : ")
umur_3023 = int(input("Masukkan Umur : "))
skor_3023 = float(input("Masukkan Skor Tes Awal : "))

# 3. Data Multiline (Alamat Domisili) & Complex Number
alamat_3023 = """Jl. Kampus Unand,
Kecamatan Pauh,
Kota Padang"""

token_3023 = complex(100, 3)

# 4. Evaluasi Status Kelulusan (Boolean)
status_lulus_3023 = skor_3023 >= BATAS_LULUS

# 5. Output Data & Tipe Data
print("\n=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")
print(f"Nama Mahasiswa  : {nama_3023} | Tipe: {type(nama_3023)}")
print(f"Jenis Kelamin   : {jk_3023} | Tipe: {type(jk_3023)}")
print("Alamat Domisili :")
print(f"{alamat_3023} | Tipe: {type(alamat_3023)}")
print(f"Umur            : {umur_3023} tahun | Tipe: {type(umur_3023)}")
print(f"Skor Tes Awal   : {skor_3023} | Tipe: {type(skor_3023)}")
print(f"ID Token Sinyal : {token_3023} | Tipe: {type(token_3023)}")

print("\n=== STATUS KELULUSAN PRAKTIKUM ===")
print(f"Batas Minimum Nilai: {BATAS_LULUS}")
print(f"Apakah Dinyatakan Lulus?: {status_lulus_3023} | Tipe: {type(status_lulus_3023)}")