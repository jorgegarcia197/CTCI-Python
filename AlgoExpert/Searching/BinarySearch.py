import math


def BinarySearch(array, target):
    if len(array) <= 0:
        return -1
    left = 0
    right = len(array)-1

    return BShelper(array, target, left, right)


def BShelper(array, target, left, right):
    if left > right:
        return -1
    middle = math.floor((left+right)/2)
    if target == array[middle]:
        return middle
    elif target < array[middle]:
        right = middle-1
        return BShelper(array, target, left, right)
    elif target > array[middle]:
        left = middle+1
        return BShelper(array, target, left, right)


def BinarySearch2(array, target):
    if len(array) <= 0:
        return -1
    left = 0
    right = len(array)-1
    while left <= right:
        middle = math.floor((left+right)/2)
        
        if target == array[middle]:
            return middle
        elif target < array[middle]:    
            right = middle-1
            continue
        elif target > array[middle]:
            left = middle+1
            continue
    return -1


if __name__ == "__main__":
    array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
    print(BinarySearch(array, 33))
