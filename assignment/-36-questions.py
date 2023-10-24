# 36. Valid Parentheses:
# Write a function that determines if a given string containing parentheses is valid.

def is_valid_parentheses(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)

    return not stack

# Example usage:
parentheses_string = "([()])"
result = is_valid_parentheses(parentheses_string)

if result:
    print("The parentheses are valid.")
else:
    print("The parentheses are not valid.")
