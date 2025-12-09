# Finger exercise: What would the code in Figure 3.4 do if the statement x = 25 were replaced by x = -25?

# x = -25
x = 25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low)/2.0

while abs((ans ** 2) - x) >= epsilon:
    numGuesses += 1
    if ans ** 2 > x:
        high = ans
    else:
        low = ans
    ans = (high + low) / 2.0
    
    print("High: ", high)
    print("Low: ", low)
print("Number of Guesses: ", numGuesses)
print("The close square root of: ", ans)

# The code behaviour is that the loop never ends
