# Given: Positive integers n≤40 and k≤5.
# Return: The total number of rabbit pairs that will be present after n months,
# if we begin with 1 pair and in each generation,
# every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
"""
A recurrence relation is a way of defining the terms of a sequence with respect to the values of previous terms.
In the case of Fibonacci's rabbits from the introduction, any given month will contain the rabbits that were alive the
previous month, plus any new offspring. A key observation is that the number of offspring in any month is equal to
the number of rabbits that were alive two months prior.
"""


def recurrence_rabbits(n: int, k: int):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if 2 < n <= 40 and k <= 5:
        return recurrence_rabbits(n-1, k) + recurrence_rabbits(n-2, k) * k
    else:
        return'None'


print(recurrence_rabbits(6, 3))
