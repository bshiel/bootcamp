import doctest
def factorial(n):
    '''Returns the factorial of n
    >>> x= 3
    >>> factorial(x)
    6
    >>> x= 4
    >>> factorial(x)
    24
    
  
    '''
    total = 1
    for i in range(1,n+1):
        total *= i
    return total
    
def fibonacci(n):
    '''Returns the Nth value in the Fibonacci
    sequence
    
    F(N) = F(N-1) + F(N-2)
    F(0) = 0, F(1) = 1
    
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(5)
    5
    '''
    assert n >= 0
    assert isinstance(n, int)
    a, b = 0, 1
    while n > 0:
        a, b = b, a+b
        n -= 1
    return a
doctest.testmod()

