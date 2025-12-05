# Finger exercise: Write a program that examines three variables—x, y, and z—and
# prints the largest odd number among them. If none of them are odd, it should
# print a message to that effect.

x = int(input("Type a number: "))
y = int(input("Type a number: "))
z = int(input("Type a number: "))

# If all numbers are even 
if x % 2 == 0 and y % 2 == 0 and z % 2 == 0:
    print("There is no odd numbers!")
    
# If x is only the even number
elif x % 2 == 0 and y % 2 != 0 and z % 2 != 0:
    if y >= z:
        print(f"{y} is the largerst odd number!")
    else:
        print(f"{z} is the largest odd number!")

# If y is only the even number
elif x % 2 != 0 and y % 2 == 0 and z % 2 != 0:
    if x >= z:
        print(f"{x} is the largest odd number!")
    else:
        print(f"{z} is the largest odd number!")

# If z is only the even number
elif x % 2 != 0 and y % 2 != 0 and z % 2 == 0:
    if x >= y:
        print(f"{x} is the largest odd number!")
    else:
        print(f"{y} is the largest odd number!")

# If x is the only odd number
elif x % 2 != 0 and y % 2 == 0 and z % 2 == 0:
    print(f"{x} is the largest odd number!")

# If y is the only odd number
elif x % 2 == 0 and y % 2 != 0 and z % 2 == 0:
    print(f"{y} is the largest odd number!")

# If z is the only odd number
elif x % 2 == 0 and y % 2 == 0 and z % 2 != 0:
    print(f"{z} is the largest odd number!")

# If all are odd numbers
elif x % 2 != 0 and y % 2 != 0 and z % 2 != 0:
    if x >= y and x >= z:
        print(f"{x} is the largest odd number!")
    elif y > z:
        print(f"{y} is the largest odd number!")
    else:
        print(f"{z} is the largest odd number!")
        
        