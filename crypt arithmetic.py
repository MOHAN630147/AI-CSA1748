import itertools

# Function to check if a given solution is valid
def is_solution_valid(s1, s2, s3, mapping):
    num1 = int("".join(str(mapping[char]) for char in s1))
    num2 = int("".join(str(mapping[char]) for char in s2))
    num3 = int("".join(str(mapping[char]) for char in s3))
    return num1 + num2 == num3

# Function to solve the cryptarithmetic problem
def solve_cryptarithmetic(s1, s2, s3):
    unique_chars = set(s1 + s2 + s3)
    
    if len(unique_chars) > 10:
        raise ValueError("Too many unique letters to map to digits")

    # Generate all possible digit permutations for the unique characters
    for perm in itertools.permutations(range(10), len(unique_chars)):
        mapping = dict(zip(unique_chars, perm))
        
        # Ensure that the first letter of any word is not mapped to 0
        if mapping[s1[0]] == 0 or mapping[s2[0]] == 0 or mapping[s3[0]] == 0:
            continue
        
        # Check if the current mapping satisfies the equation
        if is_solution_valid(s1, s2, s3, mapping):
            return mapping

    return None

def get_user_input():
    print("Enter the cryptarithmetic problem in the form: WORD1 + WORD2 = WORD3")
    s1 = input("Enter the first word (WORD1): ").strip().upper()
    s2 = input("Enter the second word (WORD2): ").strip().upper()
    s3 = input("Enter the result word (WORD3): ").strip().upper()

    return s1, s2, s3

def main():
    s1, s2, s3 = get_user_input()
    
    try:
        solution = solve_cryptarithmetic(s1, s2, s3)
        if solution:
            print(f"Solution found: {solution}")
        else:
            print("No solution found.")
    except ValueError as e:
        print(e)

# Run the program
if __name__ == "__main__":
    main()
