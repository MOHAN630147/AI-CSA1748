from itertools import permutations

# Function to calculate the total distance of a given route
def calculate_total_distance(graph, route):
    total_distance = 0
    num_cities = len(route)
    
    for i in range(num_cities - 1):
        total_distance += graph[route[i]][route[i + 1]]
    total_distance += graph[route[-1]][route[0]]  # Return to the start city

    return total_distance

# Function to solve TSP using brute-force approach
def tsp_brute_force(graph, start):
    cities = list(graph.keys())  # Get the list of cities
    cities.remove(start)  # Remove the start city from the list of permutations
    
    # Generate all possible routes (permutations) and calculate the distance for each
    min_route = None
    min_distance = float('inf')

    for route in permutations(cities):
        current_route = [start] + list(route)  # Route starting from the start city
        current_distance = calculate_total_distance(graph, current_route)

        if current_distance < min_distance:
            min_distance = current_distance
            min_route = current_route

    return min_route, min_distance

# Main function to take user input
if __name__ == "__main__":
    num_cities = int(input("Enter the number of cities: "))
    cities = []
    graph = {}

    # Input city names
    for i in range(num_cities):
        city = input(f"Enter city {i + 1} name: ")
        cities.append(city)

    # Input the distance matrix
    print("\nEnter the distance matrix:")
    for i in range(num_cities):
        graph[cities[i]] = {}
        for j in range(num_cities):
            if i != j:
                graph[cities[i]][cities[j]] = int(input(f"Distance from {cities[i]} to {cities[j]}: "))
            else:
                graph[cities[i]][cities[j]] = 0  # Distance from city to itself is 0

    start_city = input("\nEnter the starting city: ")

    # Solve TSP using brute-force approach
    route, distance = tsp_brute_force(graph, start_city)

    print("\nOptimal Route: ", " -> ".join(route))
    print(f"Minimum Distance: {distance}")
