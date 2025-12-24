def fib(n):
    """Assumes n int >= 0
    Returns Fibonacci of n"""
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def testFib(n):
    """Test no. of times that fib gets executed"""
    for i in range(n+1):
        print('fib of', i, '=', fib(i))
   
print(fib(5))
print(testFib(5))