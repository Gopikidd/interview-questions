
# 1. Rotate List:
# Rotate a list to the right by k steps.
def rotate_list(nums, k):
    n = len(nums)
    k %= n  # To handle cases where k is larger than the length of the list
    return nums[-k:] + nums[:-k]

# Example usage:
original_list = [1, 2, 3, 4, 5]
k = 2
rotated_list = rotate_list(original_list, k)

print("Original List:", original_list)
print(f"Rotated List by {k} steps:", rotated_list)
