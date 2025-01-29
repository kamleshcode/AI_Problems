def print_solution(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()

def is_safe(board, row, col):
    for i in range(col):
        if board[row][i]:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j]:
            return False
    return True

def solve_n_queens_util(board, col):
    if col >= len(board):
        print_solution(board)
        return True
    res = False
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = True
            res = solve_n_queens_util(board, col + 1) or res
            board[i][col] = False
    return res

def solve_n_queens(n):
    board = [[False for _ in range(n)] for _ in range(n)]
    if not solve_n_queens_util(board, 0):
        print("No solution exists")

n = 4
solve_n_queens(n)
