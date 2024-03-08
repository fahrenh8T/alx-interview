def pascal_triangle(n):
    """    
    Returns a list of lists of integers representing the Pascal’s triangle of n.
    Returns an empty list if n <= 0.
    Assumes n will always be an integer.
    """
    if n <= 0:
        return []
    
    ptriangle = [[1]]
    for level in range(1, n):
        row = [1]
        for i in range(1, level):
            row.append(ptriangle[level-1][i-1] + ptriangle[level-1][i])
        row.append(1)
        ptriangle.append(row)
    return ptriangle

