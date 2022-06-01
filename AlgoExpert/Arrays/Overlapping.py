def mergeOverlappingIntervals(intervals):
    # Write your code here.
    intervals = sorted(intervals, key=lambda x: x[0])
    left = 0
    right = 1
    output = []
    while left < len(intervals) and right < len(intervals):
        lower_left, upper_left = intervals[left]
        lower_right, upper_right = intervals[right]

        if lower_right < upper_left:
            # Merge intervals
            intervals[left] = [lower_left, upper_right]
            right += 1
        else:
            output.append(intervals[left])
            left = right
    output.append(intervals[left])
    return output


if __name__ == "__main__":
    input_dict = {
        "intervals": [
            [20, 21],
            [22, 23],
            [0, 1],
            [3, 4],
            [23, 24],
            [25, 27],
            [5, 6],
            [7, 19]
        ]
    }
    print(mergeOverlappingIntervals(input_dict["intervals"]))
