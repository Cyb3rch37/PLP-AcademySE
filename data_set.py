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