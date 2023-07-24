def solve_recurrence(n):
    if n <= 2:
        return n - 3 + 5 * n**2 * 2**n

    # Use memoization to store previously computed values
    memo = [None] * (n + 1)

    def recurrence_helper(k):
        if memo[k] is not None:
            return memo[k]

        result = 4 * recurrence_helper(k - 1) - 5 * recurrence_helper(k - 2) + 2 * recurrence_helper(k - 3) + k - 3 + 5 * k**2 * 2**k
        memo[k] = result
        return result

    return recurrence_helper(n)

# Test
n = 6
print(solve_recurrence(n))  # Output will be the value of T(6)
