# 14. Isomorphic Strings:
# Determine if two strings are isomorphic (i.e., same character mapping).

def isomorphic_strings(s, t):
    if len(s) != len(t):
        return False

    mapping_s_to_t = {}
    mapping_t_to_s = {}

    for char_s, char_t in zip(s, t):
        if char_s in mapping_s_to_t:
            if mapping_s_to_t[char_s] != char_t:
                return False
        else:
            mapping_s_to_t[char_s] = char_t

        if char_t in mapping_t_to_s:
            if mapping_t_to_s[char_t] != char_s:
                return False
        else:
            mapping_t_to_s[char_t] = char_s

    return True

# Example usage:
string1 = "egg"
string2 = "add"
result = isomorphic_strings(string1, string2)

print("Are the strings isomorphic?", result)
