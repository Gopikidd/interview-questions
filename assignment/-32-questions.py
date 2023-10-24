# 32. Longest Common Prefix:
# Write a function to find the longest common prefix string amongst an array of strings.

def longest_common_prefix(strings):
    if not strings:
        return ""

    # Sort the strings to ensure that the shortest string is first
    strings.sort()

    # Consider the first and last string in the sorted array
    first_str, last_str = strings[0], strings[-1]
    common_prefix = []

    for i in range(len(first_str)):
        if i < len(last_str) and first_str[i] == last_str[i]:
            common_prefix.append(first_str[i])
        else:
            break

    return ''.join(common_prefix)

# Example usage:
input_strings = ["floght", "flow",'flows' ]
result = longest_common_prefix(input_strings)

print("Longest Common Prefix:", result)

