"""
Recall the definition of the Fibonacci numbers from “Rabbits and Recurrence Relations”,
which followed the recurrence relation Fn=Fn−1+Fn−2 and assumed that each pair of rabbits reaches maturity in one month
and produces a single pair of offspring (one male, one female) each subsequent month.
Our aim is to somehow modify this recurrence relation to achieve a dynamic programming solution in the case that
all rabbits die out after a fixed number of months. See Figure 4 for a depiction of a rabbit tree in which rabbits live
for three months (meaning that they reproduce only twice before dying).
"""


# Given: Positive integers n≤100 and m≤20.
# Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.


def fibd(n: int, m: int):
    if n == 1 or n == 2:
        return 1
    generation = [0] * m
    generation[1] = 1
    for i in range (3, n+1):
        baby = sum(generation) - generation[0]
        generation = generation[-1:] + generation[:-1]
        generation[0] = baby
    return sum(generation)


print(fibd(97, 18))
