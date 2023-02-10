#!/usr/bin/python3
'''
function to find the min number occurence.
'''


def minOperations(n: int):
    '''
        minimum number of operations needed to result
        For n H characters in the file.
    '''
    if n <= 1:
        return 0
    for i in range(2, n + 1):
        if n > 1:
            n += i
            n //= 3
            if not n % 3 == 0:
                n += 3
            else:
                n += 1
    return n
