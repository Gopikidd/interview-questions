
# 5. Tuple Permutations:
# Generate all permutations of a tuple.


from itertools import permutations

def tuple_permutations(t):
    return list(permutations(t))

# Example usage:
tuple_example = (1, 2, 3, 3)
permutations_result = tuple_permutations(tuple_example)

print("Permutations of the tuple:", permutations_result)
