# 33. Merge Intervals:
# Given a collection of intervals, write a function to merge overlapping intervals.


def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])  # Sort intervals based on start times
    merged = [intervals[0]]

    for i in range(1, len(intervals)):
        current_interval = intervals[i]
        previous_interval = merged[-1]

        if current_interval[0] <= previous_interval[1]:
            # Merge the intervals
            merged[-1] = [previous_interval[0], max(previous_interval[1], current_interval[1])]
        else:
            # Add a new interval
            merged.append(current_interval)

    return merged

# Example usage:
intervals = [[1, 2], [5, 3], [4, 10], [15, 11]]
result = merge_intervals(intervals)

print("Merged Intervals:", result)
