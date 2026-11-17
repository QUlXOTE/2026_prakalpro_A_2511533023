# Name: M.Fajar Fadhilul Zikri
# NIM: 2511533023
# Question bonus
sentence = input("Masukkan kalimat: ")
cleaned = ""
for char in sentence.lower():
    if char != " ":
        cleaned += char

reversed_str = cleaned[::-1]

if cleaned == reversed_str:
    print("Palindrome")
else:
    print("Not a palindrome")