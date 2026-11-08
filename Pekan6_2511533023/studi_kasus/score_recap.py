PASS_SCORE = 60

# Target 4: minta ulang jika jumlah mahasiswa kurang dari 1
n = int(input("Number of students: "))
while n < 1:
    print("Invalid student count!")
    n = int(input("Number of students: "))

total = 0
passed = 0
highest = 0

# Target 1: baca N nilai dengan for
for i in range(1, n + 1):
    print("Student", i)
    score = int(input("Enter score: "))

    # Target 2: validasi nilai dengan while
    while score < 0 or score > 100:
        print("Invalid score!")
        score = int(input("Enter score: "))

    total += score

    # Target 3: hitung kelulusan
    if score >= PASS_SCORE:
        passed += 1

    # Varian: nilai tertinggi
    if i == 1 or score > highest:
        highest = score

average = total / n

print("Total score:", total)
print("Average score:", round(average, 2))
print("Passed:", passed)
print("Highest score:", highest)