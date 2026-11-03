# Expected output: 1, 3, 5 (one per line) 
number = 1 
  
while number <= 6:  
    number += 1 
    if number % 2 == 0: 
        continue 
    print(number) 
    