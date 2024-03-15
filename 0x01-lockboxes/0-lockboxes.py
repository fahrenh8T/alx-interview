#!/usr/bin/python3

def canUnlockAll(boxes):
    '''
    determines if all the boxes can be opened or not

    returns:
        true: all boxes can be opened
        false: not all boxes can be opened
    '''
    ttl_boxes = len(boxes)
    keys = set()
    opened_boxes = []
    crrnt_boxp = 0

    while crrnt_boxp < ttl_boxes:
        prv_boxp = crrnt_boxp
        opened_boxes.append(crrnt_boxp)
        keys.update(boxes[crrnt_boxp])
        for key in keys:
            if key != 0 and key < ttl_boxes and key not in opened_boxes:
                crrnt_boxp = key
                break
        if prv_boxp != crrnt_boxp:
            continue
        else:
            break

    for boxp in range(ttl_boxes):
        if boxp not in opened_boxes and boxp != 0:
            return False
    return True
