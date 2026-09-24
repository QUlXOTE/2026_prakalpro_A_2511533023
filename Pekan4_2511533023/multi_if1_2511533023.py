umur_3023 = int(input("Input umur Anda: "))
sim_3023 = input("Apakah anda sudah punya Sim c (y/t): ")[0]

if umur_3023 >= 17 and sim_3023 == 'y':
    print("Anda sudah dewasa dan boleh bawa motor")
if umur_3023 >= 17 and sim_3023 != 'y':
    print("Anda sudah dewasa tetapi belum tidak boleh bawa motor")
if umur_3023 < 17 and sim_3023 == 'y':
    print("Anda belum cukup umur punya sim")
if umur_3023 < 17 and sim_3023 != 'y':
    print("Anda belum cukup umur bawa motor")