# Name: M.Fajar Fadhilul Zikri
# NIM: 2511533023
# Question 5
# Bagian A

#username = input("Username: ")
# Check the rules in a safe order and print the first rule that fails.
# Messages:
#if len(username) < 5:
    #print("Invalid: at least 5 characters")
#elif not username.isalnum():
    #print("Invalid: letters and digits only")
#elif not username[0].isalpha():
    #print("Invalid: must start with a letter")
#else:
    #print("Valid")

# Bagian B 
nim = input("masukkan nim: ")
if len(nim) == 10 and nim.isdigit():
    angkatan = "20" + nim[:2]
    print(f"Valid, intake year {angkatan}")
else:
    print("Invalid NIM")