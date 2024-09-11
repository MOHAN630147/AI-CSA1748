from collections import deque

def bfs(graph, start_node):
    queue = deque([start_node])
    visited = set([start_node])
    
    while queue:
        node = queue.popleft()
        print(f"Visiting node: {node}")
        
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

def get_user_input():
    graph = {}
    
    print("Enter graph edges. Type 'done' when finished.")
    
    while True:
        node = input("Enter node name (or type 'done' to finish): ")
        if node.lower() == 'done':
            break
        
        neighbors = input(f"Enter neighbors of node {node} separated by commas (or leave blank for no neighbors): ")
        if neighbors.strip():
            neighbor_list = [n.strip() for n in neighbors.split(',')]
            graph[node] = neighbor_list
        else:
            graph[node] = []
    
    start_node = input("Enter the starting node for BFS: ")
    if start_node not in graph:
        print(f"The node {start_node} is not in the graph.")
        return None, None

    return graph, start_node

def main():
    graph, start_node = get_user_input()
    if graph and start_node:
        bfs(graph, start_node)

if __name__ == "__main__":
    main()
