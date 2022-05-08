# Write a function that takes in two array of integers and determines whether these arrays represents the same BST.Note: you are not allowed to construct any BSTs in your code


"""
    arrayOne = [10, 15, 8, 12, 94, 81, 5, 2, 11]
    arrayTwo = [10, 8, 5, 15, 2, 12, 11, 94, 81]
    output = True
"""


def sameBsts(arrayOne, arrayTwo):
    # Write your code here
    # * These are the base cases for this problem.

    # 1) If the arrays have different lengths, they cannot be the same BST.
    # 2) If the arrays are empty, they are the same BST.
    # 3) If the arrays have the same first element, at least the root its the same

    if len(arrayOne) != len(arrayTwo):
        return False
    if len(arrayOne) == 0 and len(arrayTwo) == 0:
        return True
    if arrayOne[0] != arrayTwo[0]:
        return False
    
    # * Note:
    # The way we can determine if two BSTs are the same is by getting theyre values in sorted order. We can achieve this by getting the subtree to the left by getting the smaller values and the subtree to the right by getting the larger values compared to the root.

    # Recursive calls to get the smaller and larger values for each array as if we were doing Binary Search for each subarray.
    
    # The return method of this function is True if we have reached the base case where the arrays are empty. (2nd Case). This is because we have reached the end of the arrays and we have not found a difference.

    smaller1 = getSmallerValues(arrayOne)
    smaller2 = getSmallerValues(arrayTwo)
    larger1 = getLargerValues(arrayOne)
    larger2 = getLargerValues(arrayTwo)

    return sameBsts(smaller1, smaller2) and sameBsts(larger1, larger2)




def getSmallerValues(array):
    smaller = []
    for i in range(1, len(array)):
        if array[i] < array[0]:
            smaller.append(array[i])
    return smaller


def getLargerValues(array):
    larger = []
    for i in range(1, len(array)):
        if array[i] >= array[0]:
            larger.append(array[i])
    return larger
