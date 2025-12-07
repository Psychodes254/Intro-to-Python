# Finger exercise: Write a program that asks the user to enter an integer and prints
# two integers, root and pwr, such that 0 < pwr < 6 and root**pwr is equal to the integer
# entered by the user. If no such pair of integers exists, it should print a message
# to that effect

number = int(input("Enter an integer: "))
found = False
root = 0
pwr = 1

if number == 0:
    print(f"Root = {0}")
else:
    while root ** pwr < abs(number) and not found:
        root += 1 
        for i in range(1, 6):
            if root ** i == abs(number):
                pwr = i
                found = True
                break
            
    if not found and number != 0:
        print("No pair of integers (root, pwr) exists for this number.")
    else:
        if number < 0 and pwr % 2 != 0:
            root *= -1
        print(f"Root = {root}, Power = {pwr}")

    
    