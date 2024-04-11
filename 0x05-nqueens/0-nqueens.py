#!/usr/bin/python3
'''
N Queens Challenge, script solves the problem where the goal is to place N queens on an NxN chessboard
such that no two queens threaten each other. This solution prints all possible arrangements for a given N.
'''

import sys


if __name__ == '__main__':
    # ensure proper command line arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)

    # check if N is large enough to allow a solution
    if n < 4:
        print('N must be at least 4')
        exit(1)

    solutions = []
    placed_queens = []  # coordinates format [row, column]
    stop = False
    r = 0
    c = 0

    # process each row of the board
    while r < n:
        goback = False
        # iterate each columns in the row
        while c < n:
            # assume the current column is safe until proven otherwise
            safe = True
            for cord in placed_queens:
                col = cord[1]
                if(col == c or col + (r-cord[0]) == c or
                        col - (r-cord[0]) == c):
                    safe = False
                    break

            if not safe:
                if c == n - 1:
                    goback = True
                    break
                c += 1
                continue

            cords = [r, c]
            # place queen since position is safe
            placed_queens.append(cords)
            # if this is the last row, store solution and prepare to backtrack
            if r == n - 1:
                solutions.append(placed_queens[:])
                for cord in placed_queens:
                    if cord[1] < n - 1:
                        r = cord[0]
                        c = cord[1]
                for i in range(n - r):
                    placed_queens.pop()
                if r == n - 1 and c == n - 1:
                    placed_queens = []
                    stop = True
                r -= 1
                c += 1
            else:
                c = 0
            break
        if stop:
            break
        # if no valid position in current row, backtrack to previous queen
        if goback:
            r -= 1
            while r >= 0:
                c = placed_queens[r][1] + 1
                del placed_queens[r]  # remove the last placed queen
                if c < n:
                    break
                r -= 1
            if r < 0:
                break
            continue
        r += 1

    # print all solutions
    for idx, val in enumerate(solutions):
        if idx == len(solutions) - 1:
            print(val, end='')
        else:
            print(val)
