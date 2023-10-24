# 18. Evaluate Division:
# Given equations and their corresponding values, evaluate the division and return the results in an
# array.

def div_list(val, div_num):
    out = []
    for num in val:
        temp = num // div_num
        out += [temp]
    print('division output = ', out)


value = [10, 20, 30, 40, 50, 60]
div = int(input('enter the division number = '))
div_list(value, div)


def evaluate_division(equations, values, queries):
    graph = {}

    # Build the graph
    for (numerator, denominator), value in zip(equations, values):
        if numerator not in graph:
            graph[numerator] = {}
        if denominator not in graph:
            graph[denominator] = {}
        graph[numerator][denominator] = value
        graph[denominator][numerator] = 1 / value
#
#     def dfs(start, end, visited):
#         if start not in graph or end not in graph:
#             return -1.0  # No path between start and end
#
#         if start == end:
#             return 1.0  # Same variable
#
#         visited.add(start)
#
#         for neighbor, value in graph[start].items():
#             if neighbor not in visited:
#                 result = dfs(neighbor, end, visited)
#                 if result != -1.0:
#                     return value * result
#
#         return -1.0  # No path found
#
#     results = []
#     for query_start, query_end in queries:
#         result = dfs(query_start, query_end, set())
#         results.append(result)
#
#     return results
#
# # Example usage:
# equations = [["a", "b"], ["b", "c"]]
# values = [2.0, 3.0]
# queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
#
# results = evaluate_division(equations, values, queries)
#
# print("Results:", results)
