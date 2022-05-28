def sortedSquaredArray(array):
    # Write your code here.
    left = 0
    right = len(array) - 1
    output = []
    while left <= right:
        left_value = abs(array[left])
        right_value = abs(array[right])
        chosen_one = max(left_value, right_value)
        output.insert(0, chosen_one**2)
        if chosen_one == left_value:
            left += 1
        else:
            right -= 1
    return output


if __name__ == "__main__":
    print(sortedSquaredArray([-4, -1, 0, 3, 10]))
