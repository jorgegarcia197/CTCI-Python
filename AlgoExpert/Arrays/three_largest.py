from unicodedata import name


def findThreeLargestNumbers(array):
    # Write your code here.
    largest = [None] * 3
    for value in array:
        if largest[2] is None or value > largest[2]:
            putAndUpdate(largest, value, 2)
        elif largest[1] is None or value > largest[1]:
            putAndUpdate(largest, value, 1)
        elif largest[0] is None or value > largest[0]:
            putAndUpdate(largest, value, 0)
    return largest


def putAndUpdate(arr, value, place):
    for i in range(place+1):
        if i == place:
            arr[i] = value
        else:
            arr[i] = arr[i+1]


if __name__ == "__main__":
    array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
    largest = findThreeLargestNumbers(array)
    print(largest)
