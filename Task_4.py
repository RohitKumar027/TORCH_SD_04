
def is_valid(board, row, col, num):

    if num in board[row]:
        return False


    if num in [board[i][col] for i in range(9)]:
        return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def solve_sudoku(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True

    row, col = empty_cell
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False

def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

def get_user_input():
    print("Enter the Sudoku puzzle (9 rows, each containing 9 numbers; use 0 to represent empty cells):")
    board = []
    for i in range(9):
        row = list(map(int, input().split()))
        if len(row) != 9:
            print("Each row must contain exactly 9 numbers.")
            return None
        board.append(row)
    return board

if __name__ == "__main__":
    puzzle = get_user_input()
    if puzzle:
        if solve_sudoku(puzzle):
            print("Sudoku Puzzle Solved Successfully:")
            print_board(puzzle)
        else:
            print("No solution exists for the given puzzle.")
