# Write a function isIn that accepts two strings as arguments and
# returns True if either string occurs anywhere in the other, and False otherwise.
# Hint: you might want to use the built-in str operation in.

def isIn(s1, s2):
    return (s1 in s2) or (s2 in s1)
    
    
print(isIn("cat", "concatenate"))
print(isIn("hello", "well"))
print(isIn("a", "alphabet"))
print(isIn("tree", "three"))
print(isIn("abc", "abcd"))
