class DecisionTree:
    def __init__(self, max_depth=None):
        self.max_depth = max_depth

    def fit(self, X, y):
        self.tree = self._grow_tree(X, y)

    def _gini(self, y):
        classes = set(y)
        gini = 1
        for cls in classes:
            p = (y.count(cls) / len(y))
            gini -= p ** 2
        return gini

    def _best_split(self, X, y):
        best_gini = float('inf')
        best_idx, best_val = None, None
        for idx in range(len(X[0])):
            for val in set(X[i][idx] for i in range(len(X))):
                left_mask = [X[i][idx] <= val for i in range(len(X))]
                right_mask = [X[i][idx] > val for i in range(len(X))]
                left_gini = self._gini([y[i] for i in range(len(y)) if left_mask[i]])
                right_gini = self._gini([y[i] for i in range(len(y)) if right_mask[i]])
                gini = (sum(left_mask) * left_gini + sum(right_mask) * right_gini) / len(y)
                if gini < best_gini:
                    best_gini = gini
                    best_idx = idx
                    best_val = val
        return best_idx, best_val

    def _grow_tree(self, X, y, depth=0):
        if len(set(y)) == 1 or (self.max_depth and depth == self.max_depth):
            return {'value': max(set(y), key=y.count)}
        idx, val = self._best_split(X, y)
        left_mask = [X[i][idx] <= val for i in range(len(X))]
        right_mask = [X[i][idx] > val for i in range(len(X))]
        left_tree = self._grow_tree([X[i] for i in range(len(X)) if left_mask[i]],
                                    [y[i] for i in range(len(y)) if left_mask[i]], depth + 1)
        right_tree = self._grow_tree([X[i] for i in range(len(X)) if right_mask[i]],
                                     [y[i] for i in range(len(y)) if right_mask[i]], depth + 1)
        return {'feature_idx': idx, 'threshold': val, 'left': left_tree, 'right': right_tree}

    def _predict_one(self, tree, x):
        if 'value' in tree:
            return tree['value']
        if x[tree['feature_idx']] <= tree['threshold']:
            return self._predict_one(tree['left'], x)
        else:
            return self._predict_one(tree['right'], x)

    def predict(self, X):
        return [self._predict_one(self.tree, x) for x in X]


def get_user_input():
    # Get training data from the user
    X_train = []
    y_train = []

    num_samples = int(input("Enter the number of training samples: "))
    num_features = int(input("Enter the number of features per sample: "))

    print("Enter training data (each sample on a new line, features separated by spaces):")
    for _ in range(num_samples):
        sample = list(map(float, input().split()))
        X_train.append(sample)

    print("Enter training labels (one label per sample, separated by spaces):")
    y_train = list(map(int, input().split()))

    if len(y_train) != num_samples:
        raise ValueError("Number of labels must match number of samples.")

    # Get test data from the user
    X_test = []
    num_test_samples = int(input("Enter the number of test samples: "))

    print("Enter test data (each sample on a new line, features separated by spaces):")
    for _ in range(num_test_samples):
        sample = list(map(float, input().split()))
        X_test.append(sample)

    return X_train, y_train, X_test


if __name__ == "__main__":
    X_train, y_train, X_test = get_user_input()

    clf = DecisionTree(max_depth=2)
    clf.fit(X_train, y_train)

    print("Predictions:", clf.predict(X_test))
