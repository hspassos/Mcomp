def solve_recurrence(n):
    # Use memoization to store previously computed values
    memo = {}

    def recurrence_helper(k):
        if k in memo:
            return memo[k]

        if k <= 2:
            result = k**2 + k * 2**k
        else:
            result = 5 * recurrence_helper(k - 1) - 8 * recurrence_helper(k - 2) + 4 * recurrence_helper(k - 3) + k**2 + k * 2**k + 3

        memo[k] = result
        return result

    return recurrence_helper(n)

# Test
n = 6
print(solve_recurrence(n))  # Output will be the value of T(6)
