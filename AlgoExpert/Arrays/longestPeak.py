def longestPeak(array):
    # Write your code here.
    largest = 0
    for i in range(1, len(array)-1):
        left_value = array[i-1]
        right_value = array[i+1]
        current = array[i]

        if left_value < current and right_value < current:
            # Traverse left until
            count_left = checkleft(i-1, array)
            count_right = checkright(i+1, array)
            largest = max(largest, count_left+count_right+1)
    return largest


def checkleft(left_idx, array):
    count = 1
    while left_idx > 0:
        currentValue = array[left_idx]
        next_left = array[left_idx - 1]
        if next_left >= currentValue:
            return count
        count += 1
        left_idx -= 1
    return count


def checkright(right_idx, array):
    count = 1
    while right_idx < len(array)-1:
        currentValue = array[right_idx]
        next_right = array[right_idx+1]
        if next_right >= currentValue:
            return count
        count += 1
        right_idx += 1
    return count


if __name__ == "__main__":
    input_dict = {
        "array": [5, 4, 3, 2, 1, 2, 1]
    }
    print(longestPeak(input_dict["array"]))
