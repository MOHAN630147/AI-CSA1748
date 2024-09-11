import heapq

# A* search algorithm
def a_star_search(graph, start, goal, heuristic):
    open_list = []
    heapq.heappush(open_list, (0, start))  # (priority, node)

    g_costs = {start: 0}
    # Dictionary to store the path
    came_from = {start: None}
    
    while open_list:

        current_f_cost, current_node = heapq.heappop(open_list)
        if current_node == goal:
            path = []
            while current_node:
                path.append(current_node)
                current_node = came_from[current_node]
            path.reverse()
            return path, g_costs[goal]  # Return the path and its cost
        
        # Explore neighbors
        for neighbor, cost in graph[current_node].items():
            # Calculate tentative g_cost
            tentative_g_cost = g_costs[current_node] + cost
            
            # If the tentative cost is lower than any previously recorded cost
            if neighbor not in g_costs or tentative_g_cost < g_costs[neighbor]:
                g_costs[neighbor] = tentative_g_cost
                f_cost = tentative_g_cost + heuristic[neighbor]
                heapq.heappush(open_list, (f_cost, neighbor))
                came_from[neighbor] = current_node

    return None, float('inf')  # Return None if there is no path

# Main function to take user input and run A* search
if __name__ == "__main__":
    # Graph input
    num_nodes = int(input("Enter the number of nodes: "))
    graph = {}

    for _ in range(num_nodes):
        node = input("Enter node: ")
        neighbors = input(f"Enter neighbors and their costs for {node} (format: neighbor1:cost1 neighbor2:cost2): ")
        graph[node] = {}
        for neighbor_cost in neighbors.split():
            neighbor, cost = neighbor_cost.split(":")
            graph[node][neighbor] = int(cost)

    # Heuristic input
    print("\nEnter heuristic values for each node:")
    heuristic = {}
    for _ in range(num_nodes):
        node = input(f"Enter node name: ")
        h_value = int(input(f"Enter heuristic value for {node}: "))
        heuristic[node] = h_value

    start = input("\nEnter the start node: ")
    goal = input("Enter the goal node: ")

    path, cost = a_star_search(graph, start, goal, heuristic)

    if path:
        print(f"\nPath found: {' -> '.join(path)}")
        print(f"Total cost: {cost}")
    else:
        print("No path found.")
 