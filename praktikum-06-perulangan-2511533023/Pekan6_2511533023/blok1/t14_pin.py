#hkbcejdfaig
max_attemps = 3
correct_pin = "1234"
attemp = 1

while pin != correct_pin and attemp < max_attemps:
    pin = input("enter PIN: ")
    if pin == correct_pin:
        print("Access granted")
    else:
        print("Account locked")
print("Incorrect PIN.") 
attempt += 1 