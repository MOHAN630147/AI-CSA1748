import math


def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):
    if curDepth == targetDepth:
        return scores[nodeIndex]

    if maxTurn:
        return max(minimax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth))
    else:
        return min(minimax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth))


# Function to take user input for the scores
def input_scores():
    num_scores = int(input("Enter the number of leaf nodes (must be a power of 2): "))

    # Ensure the number of scores is a power of 2
    if (num_scores & (num_scores - 1)) != 0:
        print("The number of leaf nodes must be a power of 2.")
        return None

    scores = list(map(int, input(f"Enter {num_scores} scores separated by spaces: ").split()))

    if len(scores) != num_scores:
        print(f"Please enter exactly {num_scores} scores.")
        return None

    return scores


def main():
    scores = input_scores()

    if scores is None:
        return

    # Calculate the tree depth
    treeDepth = int(math.log(len(scores), 2))

    # Call the minimax function and print the optimal value
    print("The optimal value is:", minimax(0, 0, True, scores, treeDepth))


if __name__ == "__main__":
    main()
