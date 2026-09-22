umur_3023 = int(input("Input umur Anda: "))
sim_3023 = input("Apakah anda sudah punya Sim c: ")[0]

if umur_3023 >= 17 and sim_3023 == 'y':
    print("Anda sudah dewasa dan boleh bawa motor")
elif umur_3023 >= 17 and sim_3023 != 'y':
    print("Anda sudah dewasa tetapi belum tidak boleh bawa motor")
elif umur_3023 < 17 and sim_3023 == 'y':
    print("Anda belum cukup umur punya sim")
else:
    print("Anda belum cukup umur dan tidak boleh bawa motor")
print("Program Selesai")