def join(T, R):
    res = []
    for e in R:
        res += T[e]
    return res

def canUnlockAll(boxes):
    index = 0
    total = set(boxes[0]) | {0}  # Initialize with keys from the first box
    added = True

    while added:
        added = False
        for j in join(boxes, list(total)[index:]):
            if j not in total:
                total.add(j)
                added = True

    return len(total) == len(boxes)
