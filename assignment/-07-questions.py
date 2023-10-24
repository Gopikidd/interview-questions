# 7. Power Set:
# Generate all subsets of a set

def generate_power_set(s):
    power_set = [[]]

    for element in s:
        new_subsets = [subset + [element] for subset in power_set]
        power_set.extend(new_subsets)

    return power_set

# Example usage:
set_example = {1, 2, 3}
power_set_result = generate_power_set(set_example)

print("Power Set:", power_set_result)
