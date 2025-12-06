# Finger exercise: Write a program that asks the user to enter an integer and prints
# two integers, root and pwr, such that 0 < pwr < 6 and root**pwr is equal to the integer
# entered by the user. If no such pair of integers exists, it should print a message
# to that effect

number = int(input("Enter an integer: "))
found = False
root = 0

while root ** 5 < abs(number):
    root += 1 
    for i in range(1, 5+1):
        if root ** i == abs(number):
            pwr = i
            found = True
            break
            
if not found:
    print("No pair of integers (root, pwr) exists for this number.")
else:
    if number < 0 and pwr != 2 and pwr != 4:
        root = str("-") + str(root)
    print(f"Root = {root}, Power = {pwr}")

    
    