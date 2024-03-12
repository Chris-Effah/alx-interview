#!/usr/bin/python3
"""a program based on a chess game"""
import sys

def is_safe(board, row, col, N):
    """Check if there is a queen in the same row"""
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check if there is a queen in the upper diagonal on the left
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check if there is a queen in the lower diagonal on the left
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens_util(board, col, N):
    if col == N:
        print_solution(board, N)
        return True

    res = False
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            res = solve_nqueens_util(board, col + 1, N) or res
            board[i][col] = 0

    return res

def solve_nqueens(N):
    board = [[0] * N for _ in range(N)]

    if not solve_nqueens_util(board, 0, N):
        print("No solution found")

def print_solution(board, N):
    for i in range(N):
        for j in range(N):
            print("Q" if board[i][j] else ".", end=" ")
        print()
    print()

def main():
    # Check for the correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is greater or equal to 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)

if __name__ == "__main__":
    main()

