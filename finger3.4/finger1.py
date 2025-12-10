# Finger exercise: What would have to be changed to make the code in Figure 3.4
# work for finding an approximation to the cube root of both negative and positive
# numbers? (Hint: think about changing low to ensure that the answer lies within
# the region being searched.)

x = float(input("Enter a number: "))

epsilon = 0.01
numGuesses = 0
low = min(-1.0, x)
high = max(1.0, x)

ans = (high + low)/2.0

while abs((ans ** 3) - x) >= epsilon:
    numGuesses += 1
    if ans ** 3 > x:
        high = ans
    else:
        low = ans
    ans = (high + low) / 2.0

print("Number of Guesses: ", numGuesses)
print("The close cube root of: ", ans)

