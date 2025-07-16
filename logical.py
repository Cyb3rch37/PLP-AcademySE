def sum_n(n):

    """Return the sum of the first n natural numbers using recursion."""

    if n == 0:

        return 0

    else:

        return n + sum_n(n - 1)


# Test the recursive sum against the formula: n(n+1)/2

for i in range(1, 11):

    recursive_sum = sum_n(i)

    formula_sum = i * (i + 1) // 2

    print(f"n = {i}: Recursive Sum = {recursive_sum}, Formula Sum = {formula_sum}")