import heapq

# Define the goal state
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]  # 0 represents the blank tile
]

# Define possible movements (up, down, left, right)
movements = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

# Heuristic function: Manhattan distance
def manhattan_distance(state, goal):
    # Create a dictionary to store the positions of the tiles in the goal state
    goal_positions = {value: (i, j) for i, row in enumerate(goal) for j, value in enumerate(row)}
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:  # Skip the blank tile
                goal_x, goal_y = goal_positions[state[i][j]]
                distance += abs(goal_x - i) + abs(goal_y - j)
    return distance

# Find the position of the blank (0) tile
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
    return None

# Generate possible moves
def generate_moves(state):
    blank_pos = find_blank(state)
    possible_moves = []
    for move, (dx, dy) in movements.items():
        new_blank_pos = (blank_pos[0] + dx, blank_pos[1] + dy)
        if 0 <= new_blank_pos[0] < 3 and 0 <= new_blank_pos[1] < 3:
            new_state = [row[:] for row in state]
            new_state[blank_pos[0]][blank_pos[1]], new_state[new_blank_pos[0]][new_blank_pos[1]] = \
                new_state[new_blank_pos[0]][new_blank_pos[1]], new_state[blank_pos[0]][blank_pos[1]]
            possible_moves.append((new_state, move))
    return possible_moves

# A* algorithm to solve the puzzle
def a_star(start, goal):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start, []))
    visited = set()
    while priority_queue:
        cost, state, path = heapq.heappop(priority_queue)
        if state == goal:
            return path
        visited.add(tuple(map(tuple, state)))
        for next_state, move in generate_moves(state):
            if tuple(map(tuple, next_state)) not in visited:
                heuristic = manhattan_distance(next_state, goal)
                heapq.heappush(priority_queue, (cost + 1 + heuristic, next_state, path + [move]))

                # Print the current state and the move made
                print(f"Move: {move}")
                print_state(next_state)
                print("\n")
    return None

# Helper function to print the puzzle state
def print_state(state):
    for row in state:
        print(" ".join(str(x) for x in row))

# Function to get input from user
def get_user_input():
    print("Enter the initial puzzle state (3x3 grid with numbers 0-8):")
    initial_state = []
    for i in range(3):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        if len(row) != 3 or any(x < 0 or x > 8 for x in row):
            print("Invalid input. Please enter exactly 3 numbers in the range 0-8.")
            return get_user_input()  # Recur until valid input is provided
        initial_state.append(row)
    return initial_state

# Main function
def main():
    initial_state = get_user_input()

    print("\nInitial State:")
    print_state(initial_state)
    print("\nSolving...\n")

    solution = a_star(initial_state, goal_state)

    print("Solution Path:")
    if solution:
        for move in solution:
            print(move)
    else:
        print("No solution found.")

# Run the program
if __name__ == "__main__":
    main()