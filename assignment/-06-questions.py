# 6. Tuple Sorting:
# Sort a list of tuples based on a specific index or multiple indices

def sort_tuples_by_index(lst, index):
    return sorted(lst, key=lambda x: x[index])

# Example usage:
list_of_tuples = [(1, 2, 5), (3, 1, 4), (5, 2, 3)]
index_to_sort = 2
sorted_tuples = sort_tuples_by_index(list_of_tuples, index_to_sort)

print(f"Sorted list of tuples by index {index_to_sort}: ", sorted_tuples)
