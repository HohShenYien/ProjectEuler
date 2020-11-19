'''
This is a simple function that does depth-first search and backtracking algorithm
In other words, it basically tries the values one by one until it either
completes the puzzle, or has no options left
whereby it'll hop back to previous choice and continue solving
'''

# This checks a puzzle is completed or not
# It sees if there's still any empty cell left
# Can be improvised slightly by just checking empty cells after the current
# cell, but for now, this is good enough
def complete(puzzle):
    for row in puzzle:
        for cell in row:
            if cell == 0:
                return False
    return True

# This function checks for all available non-repeated digits
# For current cell
def possible(puzzle, row, col):
    nums = set()
    # Checks for column
    for each_row in puzzle:
        if each_row[col] != 0:
            nums.add(each_row[col])

    # Checks for row
    for cell in puzzle[row]:
        if cell != 0:
            nums.add(cell)

    # This one determines which block the current cell belongs to
    # to simplify calculation
    block = col // 3 + row // 3 * 3

    # Now it checks all values in the current block
    for i in range((block // 3) * 3, (block // 3) * 3 + 3):
        for j in range((block % 3) * 3, (block % 3) * 3 + 3):
            if puzzle[i][j] != 0:
                nums.add(puzzle[i][j])

    # Then returns the complements
    return set(range(1, 10)) - nums

# The main function that does the dfs & backtracking
# It is in place
def solver_helper(puzzle, row, col):
    # Check first if this is done
    if complete(puzzle):
        return True

    # Compute the coordinate of next cell
    row_new = row
    col_new = col + 1
    if col_new == 9:
        row_new += 1
        col_new = 0

    # If the cell is not empty, move on
    if puzzle[row][col] != 0:
        return solver_helper(puzzle, row_new, col_new)

    # All the numbers available
    possibles = possible(puzzle, row, col)

    # If no more numbers available, means there's a mistake previously
    # So this path is false
    if len(possibles) == 0:
        return False

    # Trying number by number
    for val in possibles:
        puzzle[row][col] = val
        # Check if this number can be solved
        if solver_helper(puzzle, row_new, col_new):
            return True
        # If not, clean this cell
        puzzle[row][col] = 0
    return False

# Just for better syntax :P
def solver(puzzle):
    solver_helper(puzzle, 0, 0)

# Helper function to split each row into a list of 9 numbers
def split(line):
    res = []
    for i in line:
        if i != '\n':
            res.append(int(i))

    return res

# Main():
sol = 0
with open("sudoku.txt", "r") as f:
    counter = 0
    puzzle = []
    for line in f.readlines():
        # Every 10 lines is a grid
        # 1st line is Grid no.
        if counter == 0:
            counter += 1
            continue
        counter += 1
        puzzle.append(split(line))
        if counter == 10:
            solver(puzzle)
            sol += 100 * puzzle[0][0] + 10 * puzzle[0][1] + puzzle[0][2]
            puzzle = []
            counter = 0

print(sol)
