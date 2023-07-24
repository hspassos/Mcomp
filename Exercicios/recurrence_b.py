def solve_recurrence(n):
    # Use memoization to store previously computed values
    memo = {}

    def recurrence_helper(k):
        if k in memo:
            return memo[k]

        if k == 0:
            result = 0
        else:
            result = recurrence_helper(k - 1) + k**3 * 3**k

        memo[k] = result
        return result

    return recurrence_helper(n)

# Test
n = 6
print(solve_recurrence(n))  # Output will be the value of T(6)