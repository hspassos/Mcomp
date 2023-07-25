def optimal_linear_search(data, prob):
    n = len(data)

    # Initialize the table to store expected search times for each range of elements [i, j]
    A = [[0 for _ in range(n)] for _ in range(n)]

    # Calculate expected search times for single elements (base case)
    for i in range(n):
        A[i][i] = prob[i]

    # Calculate expected search times for longer ranges of elements
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            A[i][j] = float('inf')
            # Calculate the expected search time for the current range
            for k in range(i, j + 1):
                left_search_time = A[i][k - 1] if k > i else 0
                right_search_time = A[k + 1][j] if k < j else 0
                search_time = left_search_time + right_search_time
                A[i][j] = min(A[i][j], search_time)

    # The optimal search time for the entire data set is in dp[0][n-1]
    return A[0][n - 1]

# Example usage:
data = [1, 2, 3]
prob = [0.2, 0.5, 0.3]
result = optimal_linear_search(data, prob)
print("Optimal search time:", result)
