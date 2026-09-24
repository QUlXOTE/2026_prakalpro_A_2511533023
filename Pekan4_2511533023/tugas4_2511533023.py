
print("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")

# 1. Input Data Pengunjung & String Handling
nama_3023 = input("Masukkan Nama Pengunjung        : ").strip()
umur_3023 = int(input("Input umur anda                  : "))

sim_input_3023 = input("Apakah Anda Sudah Punya SIM C (y/t): ").strip().lower()
sim_3023 = sim_input_3023[0] if sim_input_3023 else 't'

# Menu Paket Wahana
print("\nPilihan Paket Wahana (1-5):")
print("  1. Safari Rimba         (Rp 50,000)")
print("  2. Arung Jeram          (Rp 75,000)")
print("  3. Motor ATV Ekstrim    (Rp 120,000)")
print("  4. Roller Coaster Kilat (Rp 100,000)")
print("  5. All-Access VIP       (Rp 220,000)")

pilihan_paket_3023 = int(input("Masukkan nomor paket (1-5)      : "))
jumlah_tiket_3023 = int(input("Masukkan jumlah tiket            : "))

# Penerapan IF Tunggal untuk Validasi Kelogisan Tiket
if jumlah_tiket_3023 <= 0:
    print("\n[Peringatan] Kuota tiket tidak valid! Jumlah tiket harus lebih dari 0.")

# 2. Pemilihan Wahana Menggunakan match - case
nama_wahana_3023 = ""
harga_satuan_3023 = 0
valid_paket_3023 = True

match pilihan_paket_3023:
    case 1:
        nama_wahana_3023 = "Wahana Safari Rimba"
        harga_satuan_3023 = 50000
    case 2:
        nama_wahana_3023 = "Wahana Arung Jeram"
        harga_satuan_3023 = 75000
    case 3:
        nama_wahana_3023 = "Wahana Motor ATV Ekstrim"
        harga_satuan_3023 = 120000
    case 4:
        nama_wahana_3023 = "Wahana Roller Coaster Kilat"
        harga_satuan_3023 = 100000
    case 5:
        nama_wahana_3023 = "Wahana All-Access VIP"
        harga_satuan_3023 = 220000
    case _:
        print("\nPaket wahana tidak valid!")
        valid_paket_3023 = False

# Jalankan sisa transaksi hanya jika pilihan paket valid dan tiket valid
if valid_paket_3023 and jumlah_tiket_3023 > 0:
    is_member_input_3023 = input("Apakah Anda member? (y/t)        : ").strip().lower()
    kode_promo_input_3023 = input("Apakah kode promo valid? (y/t)  : ").strip().lower()

    # 3. Validasi Izin Kendali Wahana Menggunakan if - elif - else dan Operator Logika
    print("\n--- KELAYAKAN PENGENDARA WAHANA ---")
    if pilihan_paket_3023 == 3:
        if umur_3023 >= 17 and sim_3023 == 'y':
            print("Status Akses: Anda sudah dewasa dan boleh mengendarai ATV sendiri.")
        elif umur_3023 >= 17 and sim_3023 != 'y':
            print("Status Akses: Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur).")
        elif umur_3023 < 17 and sim_3023 == 'y':
            print("Status Akses: Identitas tidak valid: Belum cukup umur memiliki SIM.")
        else:
            print("Status Akses: Anda belum cukup umur dan tidak boleh bawa motor ATV.")
    else:
        if umur_3023 >= 10:
            print(f"Status Akses: Anda memenuhi syarat umur untuk menikmati {nama_wahana_3023}.")
        else:
            print(f"Status Akses: Anda belum cukup umur untuk menikmati {nama_wahana_3023}.")

    # 4. Akumulasi Diskon Bertingkat Menggunakan Multi-IF Terpisah
    subtotal_3023 = harga_satuan_3023 * jumlah_tiket_3023
    total_diskon_persen_3023 = 0

    if subtotal_3023 >= 200000:
        total_diskon_persen_3023 += 10

    if is_member_input_3023 in ['y', 'ya']:
        total_diskon_persen_3023 += 5

    if kode_promo_input_3023 in ['y', 'ya']:
        total_diskon_persen_3023 += 15

    if jumlah_tiket_3023 >= 5:
        total_diskon_persen_3023 += 5

    # 5. Evaluasi Kelulusan Audit Menggunakan if - else & Output Rincian
    nominal_diskon_3023 = subtotal_3023 * (total_diskon_persen_3023 / 100)
    total_bayar_3023 = subtotal_3023 - nominal_diskon_3023

    print("\n--- Rincian Pembayaran ---")
    print(f"Subtotal Belanja : Rp {subtotal_3023:,.0f}")
    print(f"Total Diskon     : {total_diskon_persen_3023}% (Rp {nominal_diskon_3023:,.0f})")
    print(f"Total Bayar      : Rp {total_bayar_3023:,.0f}")

    if total_bayar_3023 > 300000:
        print("Catatan Layanan  : Selamat! Anda berhak mendapatkan Souvenir Gratis.")
    else:
        print("Catatan Layanan  : Terima kasih telah berkunjung.")

print("\nProgram Selesai")