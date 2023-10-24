# 15. Subarray Sum Equals K:
# Given an array of integers, find the total number of continuous subarrays whose sum equals a
# specific target number k.

def subarray_sum(nums, k):
    count = 0
    sum_dict = {0: 1}  # Initialize the dictionary with the cumulative sum 0 and its count

    current_sum = 0

    for num in nums:
        current_sum += num
        # Check if there is a subarray with the sum (current_sum - k)
        count += sum_dict.get(current_sum - k, 0)
        # Update the dictionary with the current cumulative sum
        sum_dict[current_sum] = sum_dict.get(current_sum, 0) + 1

    return count

# Example usage:
nums = [1, 2, 3, 4, 5]
k = 9

result = subarray_sum(nums, k)
print("Number of subarrays with sum", k, "is:", result)
