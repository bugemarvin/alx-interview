#!/usr/bin/python3
'''
log pahsing for display
'''


import sys


stataus_code = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0
counter = 0

try:
    for line in sys.stdin:
        my_list = line.split(" ")
        if len(my_list) > 4:
            code = my_list[-2]
            size = int(my_list[-1])
            if code in stataus_code.keys():
                stataus_code[code] += 1
            total_size += size
            counter += 1

        if counter == 10:
            counter = 0
            print('File size: {}'.format(total_size))
            for key, value in sorted(stataus_code.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as err:
    pass

finally:
    print('File size: {}'.format(total_size))
    for key, value in sorted(stataus_code.items()):
        if value != 0:
            print('{}: {}'.format(key, value))