# Name: M.Fajar Fadhilul Zikri
# NIM: 2511533023
# Question 4
phone = "082511533023"
masked = phone[:4] + "*" * (len(phone)-7) + phone[-3:]
print(masked)
