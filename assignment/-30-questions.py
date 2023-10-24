# 30. Anagram Check:
# Write a function that takes two strings as input and checks if they are anagrams of each
# other.
def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the sorted characters of both strings are equal
    return sorted(str1) == sorted(str2)

# Take user input for the two strings


string1 = input("Enter the first string: ")

string2 = input("Enter the second string: ")

if are_anagrams(string1, string2):
    print(f"{string1} and {string2} are anagrams.")
else:
    print(f"{string1} and {string2} are not anagrams.")
