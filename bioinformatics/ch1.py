#!/usr/bin/python3

moves = {"|":(-1, 0), "-":(0, -1), "\\":(-1, -1)}

def create_grid(n):
    grid = [[None for i in range(n)] for i in range(n)]
    grid[0][0] = "*" ## ultimate base case: we lose
    for row in range(n):
        for col in range(n):
            for direction, move in moves.items():
                leftA = row + move[0]
                leftB = col + move[1]
                ## well, that'd be invalid:
                if leftA < 0 or leftB < 0:
                    continue
                ## this is a winning case, take it!
                if grid[leftA][leftB] == grid[0][0]:
                    grid[row][col] = direction
            if grid[row][col] is None:
                grid[row][col] = grid[0][0] ## we lose
    return grid

## but really:
def move_to_make(row, col):
    if row % 2 == 0 and col % 2 == 0:
        return '*'
    if row % 2 and col % 2 == 0:
        return '|'
    if row % 2 == 0 and col % 2:
        return '-'
    return '\\'
