# Finger exercise: Add some code to the implementation of Newton-Raphson that
# keeps track of the number of iterations used to find the root. Use that code as
# part of a program that compares the efficiency of Newton-Raphson and bisection
# search. (You should discover that Newton-Raphson is more efficient.)

#Newton-Raphson for square root
#Find x such that x**2 - 24 is within epsilon of 0

epsilon = 0.01

k = 24.0

guess = k/2.0

num_guesses = 0

while abs(guess*guess - k) >= epsilon:
    num_guesses += 1
    guess = guess - (((guess**2) - k)/(2*guess))
    
print("Number of guesses: ", num_guesses)
print('Square root of', k, 'is about', guess)