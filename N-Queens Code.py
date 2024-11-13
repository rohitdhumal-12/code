def main():
    print("Enter No of Queens: ", end="")
    N = int(input())
    board = [[0 for _ in range(N)] for _ in range(N)]
    if helper(board, 0, N):
        print("Final Solution:")
        print_board(board)
    else:
        print("No solution exists for {} Queens".format(N))


def helper(board, col, N):
    if col >= N:
        return True
    for i in range(N):
        if is_safe(board, col, i, N):
            # Place the queen
            board[i][col] = 1
            print(f"Placing queen at row {i}, column {col}")
            print_board(board)
            print()

            # Recur to place the rest of the queens
            if helper(board, col + 1, N):
                return True

            # Backtrack: Remove the queen and print the state
            board[i][col] = 0
            print(f"Backtracking from row {i}, column {col}")
            print_board(board)
            print()
    return False


def is_safe(board, col, row, N):
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False
    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    # Check lower diagonal on the left side
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def print_board(board):
    for row in board:
        for cell in row:
            if cell == 1:
                print(" Q ", end="")
            else:
                print(" _ ", end="")
        print()


if __name__ == "__main__":
    main()
