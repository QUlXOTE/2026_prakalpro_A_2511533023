menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
number_of_days = 3
sales = []
# Write your code below
for day in range(number_of_days):
  row = []
  for menu in menus:
    porsi = int(input(f"Day {day + 1}, {menu}: "))
    row.append(porsi)
  sales.append(row)

print("Total per day:")
for r in range(len(sales)):
  day_total = 0
  for c in range(len(sales[r])):
    day_total += sales[r][c]
  print(f"Day {r + 1}: {day_total}")

menu_totals = []
for c in range(len(menus)):
  menu_total = 0
  for r in range(len(sales)):
    menu_total += sales[r][c]
  menu_totals.append((menus[c], menu_total))

print(f"Total per menu: {menu_totals}")

best_name = menu_totals[0][0]
best_total = menu_totals[0][1]
for name, total in menu_totals:
  if total > best_total:
    best_total = total
    best_name = name

print(f"Best seller: {best_name} ({best_total})")