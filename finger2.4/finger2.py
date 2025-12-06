# Finger exercise: Write a program that asks the user to input 10 integers, and then
# prints the largest odd number that was entered. If no odd number was entered, it
# should print a message to that effect.

largest_odd = None
for i in range(10):
    num = int(input("Enter a number: "))
    
    if num % 2 != 0:
        if largest_odd is None or num > largest_odd:
            largest_odd = num

if largest_odd is None:
    print("There is no odd number!")
else:
    print(f"{largest_odd} is the largest odd number!")
