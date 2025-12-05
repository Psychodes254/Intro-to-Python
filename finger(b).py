x = int(input("Type a number: "))
y = int(input("Type a number: "))
z = int(input("Type a number: "))

largest_odd = None

# Store odd number x
if x % 2 != 0:
    largest_odd = x
    
# Store odd number y
if y % 2 != 0:
    if largest_odd is None or y >= largest_odd:
        largest_odd = y
    
# Store odd number z
if z % 2 != 0:
    if largest_odd is None or z >= largest_odd:
        largest_odd = z
    
# Check the largest odd number
if largest_odd is None:
    print("There is no odd number!")
else:
    print(f"{largest_odd} is the largest odd number!")
