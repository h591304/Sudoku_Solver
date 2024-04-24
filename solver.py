# --- SUDOKU-SOLVER USING BACKTRACKING ALGORITHM ---
import numpy as np

# Example sudoku-board
board = np.array([
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ])

# Checks whether a value in a cell is possible or not based on soduko rules
def valid_solution(board, row, col, value):
    
    if board[row][col] != 0:
        return False #There exists a vaule in this cell
    if value in board[row]:
        return False #Value already exists in this row
    for c in range(len(board)):
        if board[c][col] == value:
            return False #Value already exists in this column
    
    box_x = (row // 3) * 3
    box_y = (col // 3) * 3
    for r in range(box_x, box_x + 3):
        for c in range(box_y, box_y + 3):
            if board[r][c] == value:
                return False    #Value already exists in the box
    return True

# Solves the board using backtracking recursively
def solve(board):

    # Iterate through all elements on the board to check for empty spaces
    for row in range(len(board)):
        for col in range(len(board[row])):

            # If a slot is empty, test possible values
            if board[row][col] == 0:
                for value in range(1, 10):

                    # Inserts a value if its a possible solution
                    if valid_solution(board, row, col, value):
                        board[row][col] = value

                        # Recursively solves the board
                        if solve(board):
                            return True
                        board[row][col] = 0 # Backtrack 
                return False    # There are no possible values -> backtrack for different value
    return True

solve(board)
print(board)
