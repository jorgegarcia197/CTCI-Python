def mergeOverlappingIntervals(intervals):
    # Write your code here.
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    left = 0
    right = 1
    output = []
    while left < len(intervals) and right < len(intervals):
        lower_left, upper_left = sorted_intervals[left]
        lower_right, upper_right = sorted_intervals[right]

        if lower_right <= upper_left:
            sorted_intervals[left] = [lower_left, max(upper_right, upper_left)]
            right += 1
        else:
            output.append(sorted_intervals[left])
            left = right
            right += 1
    output.append(sorted_intervals[left])
    return output

if __name__ == '__main__':
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
