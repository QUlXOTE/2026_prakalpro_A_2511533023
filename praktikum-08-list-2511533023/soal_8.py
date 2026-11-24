number_of_rows = 4
seats_per_row = 5
# Write your code below
board = []
for _ in range(number_of_rows):
  row = []
  for _ in range(seats_per_row):
    row.append(".")
  board.append(row)

seats_taken = 0

while True:
  for r in range(number_of_rows):
    line = f"Row {r + 1}:"
    for c in range(seats_per_row):
      line += " " + board[r][c]
    print(line)

  row_input = int(input("Row (0 to stop): "))
  if row_input == 0:
    break

  seat_input = int(input("Seat: "))

  if row_input < 1 or row_input > number_of_rows or seat_input < 1 or seat_input > seats_per_row:
    print("Invalid seat.")
  elif board[row_input - 1][seat_input - 1] == "X":
    print("Seat already taken.")
  else:
    board[row_input - 1][seat_input - 1] = "X"
    seats_taken += 1
    print("Seat booked.")

print(f"Seats taken: {seats_taken}")