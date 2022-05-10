def threeNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    output = []
    for idx, value in enumerate(array):
        left = idx+1
        right = len(array)-1

        while left < right:
            left_value = array[left]
            right_value = array[right]
            suma = value + left_value + right_value
            if suma == targetSum:
                output.append([value, array[left], array[right]])
                left += 1
                right -= 1
            if suma < targetSum:
                left += 1
            if suma > targetSum:
                right -= 1
    return output


if __name__ == "__main__":
    array = [12, 3, 1, 2, -6, 5, -8, 6]
    targetSum = 0
    print(threeNumberSum(array, targetSum))
