tinggi_3023 = int(input("Masukkan tinggi pola (bilangan genap, misalnya 10): "))

if tinggi_3023 % 2 != 0:
    print("Tinggi harus bilangan genap")
else:
    a_3023 = tinggi_3023 - 2
    c_3023 = a_3023
    lebar_3023 = (2 * tinggi_3023) - 2

    for i_3023 in range(1, tinggi_3023 + 1):
        b_3023 = c_3023 + 1

        for j_3023 in range(1, lebar_3023 + 1):

            # Baris atas dan bawah
            if i_3023 == 1 or i_3023 == tinggi_3023:
                if j_3023 == 1 or j_3023 == lebar_3023:
                    print("#", end="")
                else:
                    print("=", end="")

            # Baris isi
            else:
                if j_3023 == 1 or j_3023 == lebar_3023:
                    print("|", end="")
                else:
                    if j_3023 == c_3023:
                        print("<", end="")
                    elif j_3023 == b_3023:
                        print(">", end="")
                    elif j_3023 == (lebar_3023 - c_3023):
                        print("<", end="")
                    elif j_3023 == (lebar_3023 - c_3023 + 1):
                        print(">", end="")
                    elif j_3023 > b_3023 and j_3023 < (lebar_3023 - c_3023):
                        print(".", end="")
                    else:
                        print(" ", end="")

        print()

        # Logika asli Java
        a_3023 -= 2

        if a_3023 <= 0:
            c_3023 = (-a_3023) + 2
        else:
            c_3023 = a_3023