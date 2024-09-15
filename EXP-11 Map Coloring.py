class MapColoringCSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints

    def is_consistent(self, variable, value, assignment):
        for neighbor in self.constraints.get(variable, []):
            if neighbor in assignment and assignment[neighbor] == value:
                return False
        return True

    def backtracking_search(self, assignment={}):
        if len(assignment) == len(self.variables):
            return assignment

        unassigned_variables = [v for v in self.variables if v not in assignment]
        var = unassigned_variables[0]

        for value in self.domains[var]:
            if self.is_consistent(var, value, assignment):
                assignment[var] = value
                result = self.backtracking_search(assignment)
                if result is not None:
                    return result
                assignment.pop(var)

        return None


def input_data():
    # Input variables
    variables = input("Enter the regions (variables) separated by spaces: ").split()

    # Input domains
    domains = {}
    for var in variables:
        domain = input(f"Enter the available colors for {var} separated by spaces: ").split()
        domains[var] = domain

    # Input constraints
    constraints = {}
    for var in variables:
        neighbors = input(f"Enter the neighbors of {var} separated by spaces: ").split()
        constraints[var] = neighbors

    return variables, domains, constraints


def main():
    variables, domains, constraints = input_data()

    csp = MapColoringCSP(variables, domains, constraints)
    assignment = csp.backtracking_search()

    if assignment:
        print("Solution found:")
        for var, value in assignment.items():
            print(f"{var}: {value}")
    else:
        print("No solution found.")


if __name__ == "__main__":
    main()
