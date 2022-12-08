"""
A permutation of length n is an ordering of the positive integers {1,2,…,n}.
For example, π=(5,3,2,1,4) is a permutation of length 5.

Given: A positive integer n≤7.
Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).
"""


def permutation(input_list: list[int]):
    if len(input_list) == 2:
        list1 = input_list.copy()
        input_list.reverse()
        result = [list1, input_list]
        return result
    total =[]
    for i in range(0, len(input_list)):
        list1 = input_list.copy()
        list1.pop(i)
        result = permutation(list1)

        for j in result:
            j.insert(0, input_list[i])

        total.extend(result)
    return total


def print_perm(input_list: list[int]):
    list1 = permutation(input_list)
    print(len(list1))
    for i in list1:
        s = [str(num) for num in i]
        print(' '.join(s))


print_perm([1, 2, 3, 4, 5])
