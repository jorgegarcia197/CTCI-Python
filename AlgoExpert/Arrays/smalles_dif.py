

def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()
    onepointer = 0
    twopointer = 0
    smallestPair = []
    smallest = float("inf")

    while onepointer < len(arrayOne) and twopointer < len(arrayTwo):
        one_value = arrayOne[onepointer]
        two_value = arrayTwo[twopointer]
        diff = abs(two_value - one_value)
        if one_value < two_value:
            onepointer += 1
        elif one_value > two_value:
            twopointer += 1
        else:
            return [one_value, two_value]
        if smallest > diff:
            smallest = diff
            smallestPair = [one_value, two_value]
    return smallestPair


if __name__ == '__main__':
    input_dict = {
        "arrayOne": [-1, 5, 10, 20, 28, 3],
        "arrayTwo": [26, 134, 135, 15, 17]
    }
    print(smallestDifference(input_dict["arrayOne"], input_dict["arrayTwo"]))
