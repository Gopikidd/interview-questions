# 19. Longest Substring with at Most K Distinct Characters:
# Given a string, find the length of the longest substring T that contains at most k distinct characters.

def k_distinct(s, k):
    if k == 0:
        return 0

    char_count = {}
    start = 0
    max_length = 0

    for end in range(len(s)):
        char_count[s[end]] = char_count.get(s[end], 0) + 1

        while len(char_count) > k:
            char_count[s[start]] -= 1
            if char_count[s[start]] == 0:
                del char_count[s[start]]
            start += 1

        max_length = max(max_length, end - start + 1)

    return max_length


# Example usage:
input_string = "eceba"
k = 2
result = k_distinct(input_string, k)

print(f"The length of the longest substring with at most {k} distinct characters is {result}.")
