from collections import deque

def is_valid_state(m, c):
    # Missionaries must never be outnumbered by cannibals on either side of the river
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    if (m > 0 and m < c):  # On the left side, cannibals can't outnumber missionaries
        return False
    if (3 - m > 0 and 3 - m < 3 - c):  # On the right side, same constraint applies
        return False
    return True

def get_possible_moves(state):
    m, c, boat = state
    possible_moves = []
    if boat == 1:  # Boat is on the left side
        new_states = [(m - 2, c, 0, "2M"), (m - 1, c, 0, "1M"), (m, c - 2, 0, "2C"), 
                      (m, c - 1, 0, "1C"), (m - 1, c - 1, 0, "1M 1C")]
    else:  # Boat is on the right side
        new_states = [(m + 2, c, 1, "2M"), (m + 1, c, 1, "1M"), (m, c + 2, 1, "2C"), 
                      (m, c + 1, 1, "1C"), (m + 1, c + 1, 1, "1M 1C")]
    
    valid_moves = []
    for new_state in new_states:
        if is_valid_state(new_state[0], new_state[1]):
            valid_moves.append(new_state)
    
    return valid_moves

def missionaries_and_cannibals_bfs(initial_state, goal_state):
    queue = deque([(initial_state, [])])  # Queue stores (current state, path to state)
    visited = set()  # To keep track of visited states
    visited.add(initial_state)

    while queue:
        state, path = queue.popleft()

        if state[:3] == goal_state:
            return path + [state]

        for next_state in get_possible_moves(state):
            if next_state[:3] not in visited:
                visited.add(next_state[:3])
                queue.append((next_state[:3], path + [(state, next_state[3])]))

    return None

def get_user_input():
    while True:
        try:
            m_left = int(input("Enter the number of missionaries on the left side (initial state): "))
            c_left = int(input("Enter the number of cannibals on the left side (initial state): "))
            boat_pos = int(input("Enter the initial position of the boat (1 for left, 0 for right): "))

            if m_left < 0 or c_left < 0 or boat_pos not in (0, 1):
                print("Invalid input. Please enter non-negative numbers for missionaries and cannibals, and 1 or 0 for boat position.")
                continue

            initial_state = (m_left, c_left, boat_pos)
            goal_state = (0, 0, 0)  # The goal state is always to move all to the right side

            return initial_state, goal_state

        except ValueError:
            print("Invalid input. Please enter valid integers.")

def print_solution(solution):
    if solution:
        print("Solution found:")
        for step in solution:
            if len(step) == 2:
                current_state, move = step
                print(f"{current_state} -> {move} moved")
            else:
                print(f"{step} (Goal)")
    else:
        print("No solution found.")

def main():
    initial_state, goal_state = get_user_input()
    solution = missionaries_and_cannibals_bfs(initial_state, goal_state)
    print_solution(solution)

if __name__ == "__main__":
    main()