#!/usr/bin/python3
'''
function to find the min number occurence.
'''


def minOperations(n: int):
    '''
        minimum number of operations needed to result
        For n H characters in the file.
    '''
    counter = 2
    oper = 0
    if n <= 1:
        return 0
    else:
        while n > 1:
            while n % counter == 0:
                oper += counter
                n //= counter
            counter += 1
        return oper
