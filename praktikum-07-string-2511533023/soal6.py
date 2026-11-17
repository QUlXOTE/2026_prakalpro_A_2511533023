# Name: M.Fajar Fadhilul Zikri
# NIM: 2511533023
# Question 6
#first_name = " muhammad"
#last_name = "rafi "
#full_name = first_name.strip() + " " + last_name.strip()
#print(full_name)
#print(full_name.title())

full_name = "Kartika"
nim = "2511533023"
clean_name = full_name.strip()
space_idx = clean_name.find(" ")
if space_idx == -1:
    first_name = clean_name
else:
    first_name = clean_name[:space_idx]

username = first_name.lower() + nim[-3:]
print(username)

 
# Build the username: first name in lowercase + last 3 digits of the NIM.
# Do not use split().
