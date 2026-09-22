total_belanja_3023 = float(input("Masukkan total belanja (Rp): "))

input_member_3023 = input("Apakah anda member? (y/t): ").strip().lower()
is_member_3023 = input_member_3023 in ["y", "ya"]

input_promo_3023 = input("Apakah kode promo valid? (y/t): ").strip().lower()
kode_promo_valid_3023 = input_promo_3023 in ["y", "ya"]

total_diskon_persen_3023 = 0

if total_belanja_3023 > 1000000:
    total_diskon_persen_3023 += 10
if is_member_3023:
    total_diskon_persen_3023 += 5
if kode_promo_valid_3023:
    total_diskon_persen_3023 += 15

nominal_diskon_3023 = total_belanja_3023 * (total_diskon_persen_3023 / 100)
total_bayar_3023 = total_belanja_3023 - nominal_diskon_3023

print("\n---Rincian Pembayaran---")
print(f"Total Diskon : {total_diskon_persen_3023}% (Rp {nominal_diskon_3023:,.0f})")
print(f"Total Bayar : Rp {total_bayar_3023:,.0f}")

print(f"Total Diskon yang anda dapatkan: {total_diskon_persen_3023}%")