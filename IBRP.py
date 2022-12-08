"""
Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms
k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual possessing
a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate
"""
from itertools import combinations


def mendel_pr(k: int, m: int, n: int):
    s = k + m + n
    pr_m_1 = m / s
    pr_m_2 = (m-1)/(s-1)
    pr_m_3 = m/(s-1)
    pr_n_1 = n / s
    pr_n_2 = (n-1)/(s-1)
    pr_n_3 = n/(s-1)
    a = pr_n_1 * pr_n_2
    b = pr_m_1 * pr_n_3 * 0.5 + pr_n_1 * pr_m_3 * 0.5
    c = pr_m_1 * pr_m_2 * 1/4
    return 1 - (a+b+c)


print(mendel_pr(16, 26, 22))
