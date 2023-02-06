#!/usr/bin/python3
'''
breadth-first search (BFS) algorithm to determine if all boxes can be opened.
'''


def canUnlockAll(boxes):
    '''
            function for boxes
            boxes is a list of a list
    '''
    my_boxes = [0]  # my stack
    numbers = [False] * len(boxes)
    numbers[0] = True
    for box in my_boxes:
        for key in boxes[box]:
            if key < len(numbers) and not numbers[key]:
                numbers[key] = True
                my_boxes.append(key)
    return len(my_boxes) == len(boxes)
