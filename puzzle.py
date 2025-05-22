def is_safe(board, row, col, n):
    # All 8 possible moves of a knight
    moves = [
        (-2, -1), (-2, 1),
        (-1, -2), (-1, 2),
        (1, -2),  (1, 2),
        (2, -1),  (2, 1)
    ]

    for dr, dc in moves:
        r, c = row + dr, col + dc
        if 0 <= r < n and 0 <= c < n and board[r][c] == 1:
            return False
    return True

def solve_knights(board, n, knights_placed=0, row=0, col=0):
    if knights_placed == n:
        return True

    for i in range(row, n):
        for j in range(n):
            if board[i][j] == 0 and is_safe(board, i, j, n):
                board[i][j] = 1
                if solve_knights(board, n, knights_placed + 1, i, j):
                    return True
                board[i][j] = 0
    return False

def print_board(board):
    for row in board:
        print(" ".join("K" if cell == 1 else "." for cell in row))
    print()

# Entry point
if __name__ == "__main__":
    n = int(input("Enter the size of the board (n x n): "))
    board = [[0 for _ in range(n)] for _ in range(n)]

    if solve_knights(board, n):
        print(f"\nSolution for {n} knights on a {n}x{n} board:")
        print_board(board)
    else:
        print(f"No solution found for placing {n} knights safely.")
