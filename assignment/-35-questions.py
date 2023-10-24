# # 35. Two Sum Problem:
# # Given an array of integers, find two numbers such that they add up to a specific target
# # number.
#
# def sume_trget(li):
#     pass
#
#
#
#
#
# temp = []
# for i in range(1,100):
#     temp= [i]
#
# sume_trget(temp)
#
#
def two_sum(nums, target):
    num_indices = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_indices:
            return [num_indices[complement], i]
        num_indices[num] = i

    return None  # No solution found

# Example usage:
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)

if result is not None:
    print(f"The indices of the two numbers that add up to {target} are {result}.")
else:
    print(f"No solution found.")
