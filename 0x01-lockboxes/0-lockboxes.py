#!/usr/bin/python3

def canUnlockAll(boxes):
    '''
    determines if all the boxes can be opened or not

    returns:
        true: all boxes can be opened
        false: not all boxes can be opened
    '''
    opened = {0}
    keys = boxes[0]
    
    while keys:
        newKeys = []
        for key in keys:
            if key not in opened and key < len(boxes):
                opened.add(key)
                newKeys.extend(boxes[key])
        keys = newKeys

    return len(opened) == len(boxes)
