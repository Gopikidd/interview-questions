# 2. Minimum Window Sublist:
# Find the minimum window in a list that contafrom collections import Counter
#
from collections import Counter


def min_window_sublist(s, t):
    target_count = Counter(t)
    required_chars = len(target_count)

    left, right = 0, 0
    formed_chars = 0
    current_window = Counter()
    result = float('inf'), None, None

    while right < len(s):
        char = s[right]
        current_window[char] += 1
        if char in target_count and current_window[char] == target_count[char]:
            formed_chars += 1

        while formed_chars == required_chars:
            if right - left + 1 < result[0]:
                result = right - left + 1, left, right + 1

            char_left = s[left]
            current_window[char_left] -= 1
            if char_left in target_count and current_window[char_left] < target_count[char_left]:
                formed_chars -= 1

            left += 1

        right += 1

    return s[result[1]:result[2]] if result[0] != float('inf') else ""


# Example usage:
s = "ADOBECODEBANC"
t = "ABC"
min_window = min_window_sublist(s, t)

print("Minimum Window Sublist:", min_window)
