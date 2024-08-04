# 2a Write a program to simulate 4-Queen / N-Queen problem.

# N-Queen Problem Characteristics
# - Time Complexity: The time complexity of the N-Queen problem is O(N!), as there are N choices for the first queen, N-1 choices for the second, and so on.
# - Space Complexity: The space complexity is O(N^2) for storing the board.

def is_safe(board, row, col, N):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # # Check lower diagonal on left side
    # for i, j in zip(range(row, N, 1), range(col, -1, -1)):
    #     if board[i][j] == 1:
    #         return False

    return True

def solve_n_queens(board, col, N):
    # If all queens are placed, return True
    if col >= N:
        return True

    # Consider this column and try placing this queen in all rows one by one
    for i in range(N):
        if is_safe(board, i, col, N):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # Recur to place rest of the queens
            if solve_n_queens(board, col + 1, N):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution,
            # then remove the queen (backtrack)
            board[i][col] = 0

    # If the queen cannot be placed in any row in this column, return False
    return False

def n_queens(N):
    board = [[0] * N for _ in range(N)]
    
    # print(len(board))
    # return

    if not solve_n_queens(board, 0, N):
        print("Solution does not exist")
        return False

    # Print the solution
    for row in board:
        print(" ".join("Q" if x else "." for x in row))
    return True

# Example usage:
N = 5
print(f"{N}-Queen Problem Solution:")
n_queens(N)
