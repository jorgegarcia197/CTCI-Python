def moveElementToEnd(array, toMove):
    # Write your code here.
    if not array:
        return []
    left = 0
    right = len(array)-1
    if array[0] == toMove:
        array.pop(0)
        array.append(toMove)
    while array[right] == toMove and right > 0:
        right -= 1
    while left < right:
        if array[left] == toMove:
            array[left], array[right] = array[right], array[left]
            right -= 1
        else:
            left += 1
    return array


if __name__ == '__main__':
    input_dict = {
        "array": [],
        "toMove": 2
    }
    print(moveElementToEnd(input_dict["array"], input_dict["toMove"]))
