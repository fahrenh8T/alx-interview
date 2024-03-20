#!/usr/bin/python3

def canUnlockAll(boxes):
    '''
    determines if all the boxes can be opened or not

    returns:
        true: all boxes can be opened
        false: not all boxes can be opened
    '''
    openedBoxes = set([0])
    keys = set(boxes[0])
    
    while keys:
        newKeys = set()
        for key in keys:
            if key < len(boxes) and key not in openedBoxes:
                openedBoxes.add(key)
                newKeys.update(boxes[key])
        keys = newKeys

    return len(openedBoxes) == len(boxes)
