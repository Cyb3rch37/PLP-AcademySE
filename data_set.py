# Define two sets

A = {1, 2, 3, 4}

B = {3, 4, 5, 6}

# Set operations in action

union_set = A.union(B)# Alternatively: A | B

intersection_set = A.intersection(B)# Alternatively: A & B

difference_set = A.difference(B)# Alternatively: A - B


print("Set A:", A)

print("Set B:", B)

print("Union:", union_set)

print("Intersection:", intersection_set)

print("Difference (A - B):", difference_set)

"""
| Operation           | Description                     | Symbol  | Example Result |             |
| ------------------- | ------------------------------- | ------- | -------------- | ----------- |
| `a.union(b)`        | All items from both sets        | \`a     | b\`            | `{1,2,3,4,5,6}` |
| `a.intersection(b)` | Items in **both** sets          | `a & b` | `{3,4}`        |             |
| `a.difference(b)`   | Items in `a` but **not in** `b` | `a - b` | `{1,2}`          |             |

Explanation: This function models the inductive step: if you assume the formula holds for n - 1, then adding n should yield the correct answer for n. The printed comparison verifies the correctness over several test cases.

"""