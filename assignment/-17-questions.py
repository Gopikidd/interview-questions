# 17. First Missing Positive:
# Given an unsorted integer array, find the smallest missing positive integer.

def small_missing(val):
    out = []
    for num in val:

        if num > 1:
            out.append(num)
            re = sorted(out)
        result = re[0] - 1
    print(result)
#
#
# user_inp = [8, 3, 4, 5, -1, -4]
# small_missing(user_inp)
#

# def first_missing_positive(nums):
#     n = len(nums)
#
#     for i in range(n):
#         while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
#             nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
#
#     for i in range(n):
#         if nums[i] != i + 1:
#             return i + 1
#
#     return n + 1
#
# # Example usage:
# user_inp = [ 4, 5, 1, -1, -4, -7]
# result = first_missing_positive(user_inp)
#
# print("The smallest missing positive integer is:", result)
