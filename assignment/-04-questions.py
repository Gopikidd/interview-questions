
# 4. Next Permutation:
# Implement the next permutation, which rearranges numbers into the lexicographically next greater
# permutation.

def next_permutation(nums):
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i >= 0:
        j = len(nums) - 1
        while j >= 0 and nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]

    nums[i + 1:] = reversed(nums[i + 1:])

# Example usage:
perm_list = [1, 2, 3]
next_permutation(perm_list)

print("Next Permutation:", perm_list)
