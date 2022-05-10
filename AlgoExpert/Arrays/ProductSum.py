def productSum(array):
    # Write your code here.
    level = 1
    suma = 0
    for value in array:
        if isinstance(value, list):
            # Get inner array first
            suma += getInnerArray(value, level+1)
        else:
            suma += value
    return suma


def getInnerArray(inner, level):
    innersum = 0
    for value in inner:
        if isinstance(value, list):
            innersum += getInnerArray(value, level+1)
        else:
            innersum += value
    return level * innersum


if __name__ == "__main__":
    print(productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]))
