# 1/usr/bin/python3
'''
function to find the min number of H occurence.
'''
import sys


def minOperations(n):
    '''
    creating a copy list to store the n occurence
    Initializing the 1st index to 2 and power of 2
    To loop through starting at point 2 of the index
    till the nth occurence and the null terminator
    '''
    if n <= 1:
        return 0
    total = 0
    for a in range(2, n + 1):
        if n % a == 0:
            total += 1
            n //= a
    return total
