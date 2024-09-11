def is_safe(board, row, col):
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, col):
    # Base case: If all queens are placed
    if col >= len(board):
        return True

    # Try placing a queen in all rows one by one in the current column
    for i in range(len(board)):
        if is_safe(board, i, col):
            # Place the queen
            board[i][col] = 1

            # Recur to place the rest of the queens
            if solve_n_queens_util(board, col + 1):
                return True

            # If placing the queen in this position doesn't lead to a solution
            # Backtrack and remove the queen from this position
            board[i][col] = 0

    return False

def solve_n_queens(N):
    # Initialize the board with zeros
    board = [[0 for _ in range(N)] for _ in range(N)]

    if solve_n_queens_util(board, 0):
        print_board(board)
    else:
        print("No solution exists")

def print_board(board):
    for row in board:
        print(" ".join(str(x) for x in row))
    print("\n")

# Function to get the board size from the user
def get_user_input():
    while True:
        try:
            N = int(input("Enter the size of the chessboard (N): "))
            if N >= 4:
                return N
            else:
                print("N should be at least 4 to have a valid solution. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Main function
def main():
    N = get_user_input()  # Get the board size from the user
    solve_n_queens(N)  # Solve the N-Queens problem for the user-defined board size

# Run the program
if __name__ == "__main__":
    main()