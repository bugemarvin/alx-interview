#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 21
print("Min # of operations --> 10 to reach {} char: {}".format(n, minOperations(n)))

n = 9
print("Min # of operations --> 6 to reach {} char: {}".format(n, minOperations(n)))

n = 972
print("Min # of operations --> 19 to reach {} char: {}".format(n, minOperations(n)))

n = 2147483640
print("Min # of operations --> 326 to reach {} char: {}".format(n, minOperations(n)))
