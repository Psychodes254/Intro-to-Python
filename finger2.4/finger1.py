# Finger exercise: Replace the comment in the following code with a while loop.

numXs = int(input('How many times should I print the letter X? '))
toPrint = ''
count = 0

while count < numXs:
    count += 1
    toPrint += "x"
    
print(toPrint)

