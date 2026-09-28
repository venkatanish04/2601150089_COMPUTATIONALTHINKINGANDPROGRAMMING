# 0/1 Knapsack using Dynamic Programming

def knapsack(weights, values, capacity):
    n = len(weights)

    # Create DP table
    dp = [[0 for _ in range(capacity + 1)]
          for _ in range(n + 1)]

    # Build the DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):

            # If current item can fit
            if weights[i - 1] <= w:
                include = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                exclude = dp[i - 1][w]

                dp[i][w] = max(include, exclude)

            # If current item cannot fit
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# Main program
n = int(input("Enter number of items: "))

weights = list(map(int, input("Enter weights: ").split()))
values = list(map(int, input("Enter values: ").split()))

capacity = int(input("Enter knapsack capacity: "))

max_value = knapsack(weights, values, capacity)

print("Maximum value:", max_value)

print("\nTime Complexity: O(n * W)")
print("Space Complexity: O(n * W)")