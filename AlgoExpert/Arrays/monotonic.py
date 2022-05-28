def isMonotonic(array):
    # Write your code here.
    if len(array) <= 1:
        return True

    # check for trend
    if array[1] >= array[0]:
        ascending = True
        last = float("-inf")

    elif array[1] <= array[0]:
        ascending = False
        last = float("inf")

    for idx, value in enumerate(array):
        if ascending:
            if value < last:
                return False
        else:
            if value > last:
                return False
        last = value
    return True


def isMonotonic2(array):
    if len(array) <= 1:
        return True
    direction = array[1] - array[0]
    for i in range(2, len(array)):
        if direction == 0:
            direction = array[i] - array[i-1]
            continue
        if breakdDir(direction, array[i] - array[i-1]):
            return False
    return True


def breakdDir(direction, newDirection):
    if direction > 0:
        return newDirection < 0
    return newDirection > 0


if __name__ == '__main__':
    input_array = {
        "array": [-1, -1, -2, -3, -4, -5, -5, -5, -6, -7, -8, -8, -9, -10, -11]
    }
    print(isMonotonic2(input_array["array"]))
