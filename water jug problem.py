from collections import deque

def is_goal(state, target):
    return state[0] == target or state[1] == target

def get_successors(state, capacities):
    successors = []
    jug1, jug2 = state
    max1, max2 = capacities

    # Fill jug 1
    successors.append((max1, jug2))
    # Fill jug 2
    successors.append((jug1, max2))
    # Empty jug 1
    successors.append((0, jug2))
    # Empty jug 2
    successors.append((jug1, 0))
    # Pour jug 1 into jug 2
    pour = min(jug1, max2 - jug2)
    successors.append((jug1 - pour, jug2 + pour))
    # Pour jug 2 into jug 1
    pour = min(jug2, max1 - jug1)
    successors.append((jug1 + pour, jug2 - pour))

    return successors

def bfs(capacities, target):
    start_state = (0, 0)
    queue = deque([(start_state, [])])
    visited = set()

    while queue:
        current_state, path = queue.popleft()

        if is_goal(current_state, target):
            return path + [current_state]

        if current_state in visited:
            continue

        visited.add(current_state)

        for next_state in get_successors(current_state, capacities):
            if next_state not in visited:
                queue.append((next_state, path + [current_state]))

    return None

def print_solution(solution):
    if solution:
        for step, state in enumerate(solution):
            print(f"Step {step}: Jug 1 = {state[0]} liters, Jug 2 = {state[1]} liters")
    else:
        print("No solution found.")

def get_user_input():
    while True:
        try:
            max1 = int(input("Enter the capacity of Jug 1 (liters): "))
            max2 = int(input("Enter the capacity of Jug 2 (liters): "))
            target = int(input("Enter the target amount of water (liters): "))

            if max1 <= 0 or max2 <= 0 or target < 0:
                print("All capacities and target must be positive integers. Please try again.")
                continue

            return (max1, max2), target

        except ValueError:
            print("Invalid input. Please enter valid integers.")

def main():
    capacities, target = get_user_input()
    solution = bfs(capacities, target)
    print_solution(solution)

# Run the program
if __name__ == "__main__":
    main()