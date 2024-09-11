# DFS algorithm in Python with user input

# Function to perform DFS
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()  # Keeps track of visited nodes
    visited.add(start)
    
    print(start, end=" ")  # Process the current node

    # Recursively visit adjacent nodes
    for neighbor in graph.get(start, []):
        if neighbor not in visited and neighbor in graph:
            dfs(graph, neighbor, visited)

# Function to take user input for graph
def take_graph_input():
    graph = {}
    num_nodes = int(input("Enter the number of nodes: "))

    for _ in range(num_nodes):
        node = input("Enter node: ")
        neighbors = input(f"Enter neighbors of {node} (space-separated): ").split()
        graph[node] = neighbors

    return graph

# Main function
if __name__ == "__main__":
    graph = take_graph_input()
    start_node = input("Enter the start node for DFS: ")

    print("\nDFS traversal: ")
    dfs(graph, start_node)
