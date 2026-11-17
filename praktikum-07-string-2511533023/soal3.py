# Name: M.Fajar Fadhilul Zikri
# NIM: 2511533023
# Question 3
# Bagian A
#text = "Informatika"
#print(text[11]) -> perbaikan gunakan indeks dari 0-10
#print(text.upper) -> perbaikan print(text.upper())
#print(text[0:20]) 

text = "M.Fajar Fadhilul Zikri"
count = 0
for char in text.lower():
    if char in "aiueo":
        count += 1
print("Vowels:", count)
