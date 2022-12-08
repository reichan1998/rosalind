"""
The Fibonacci numbers 0,1,1,2,3,5,8,13,21,34,… are generated by the following simple rule
Fn=⎧⎩⎨Fn−1+Fn−2,1,0,n>1,n=1,n=0.

Given: A positive integer n≤25.

Return: The value of Fn.

Source: Algorithms by Dasgupta, Papadimitriou, Vazirani. McGraw-Hill. 2006.
"""


def fibonacci(n: int):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return n
    if n > 1:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(24))