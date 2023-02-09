# 1/usr/bin/python3
'''
function to find the min number occurence.
'''


def minOperations(n):
    '''
        minimum number of operations needed to result
        For n H characters in the file.
    '''
    count = 0
    while n > 1:
        f = 2
        while f * f <= n:
            if n % f == 0:
                break
            f += 1
        if f * f > n:
            f = n
        while n % f == 0:
            count += 1
            n /= f
    return count

