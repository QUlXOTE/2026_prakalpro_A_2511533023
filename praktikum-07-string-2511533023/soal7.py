# Name: M.Fajar Fadhilul Zikri
# NIM: 2511533023
# Question 7
full_name = "M.Fajar Fadhilul Zikri"
nim = "2511533023"

clean_name = full_name.strip()
space_idx = clean_name.find(" ")
first_name = clean_name if space_idx == -1 else clean_name[:space_idx]
username = first_name.lower() + nim[-3:]
intake_year = "20" + nim[:2]

card_width = 30
title_text = "STUDENT CARD"

print("=" * card_width)
print(title_text.center(card_width))
print("=" * card_width)
print(f"{'Name':<10}: {clean_name.title()}")
print(f"{'NIM':<10}: {nim}")
print(f"{'Username':<10}: {username}")
print(f"{'Intake':<10}: {intake_year}")
print("=" * card_width)