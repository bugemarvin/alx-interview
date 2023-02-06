#!/usr/bin/python3
'''
n number locked boxes.
Each box is numbered sequentially and may contain keys to other boxes.
A key with the same number as a box opens that box
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked
Return True if all boxes can be opened, else return False
'''


def canUnlockAll(boxes):
    '''
            function for boxes
            boxes is a list of a list
    '''
    boxes_size = len(boxes)
    my_boxes = [0]
    for index, keys in enumerate(boxes):
        for values in range(len(keys)):
            my_boxes.append(keys[values])
    my_list = len(set(my_boxes))
    if my_list == boxes_size:
        return True
    else:
        return False
