def threeNumberSort(array, order):
    # Write your code here.
    # What I think to do is to count the number of times every item is in the array

    for idx, number in enumerate(order):
        count = array.count(number)
        order[idx] = (count, number)
    idx = 0
    for count, number in order:
        array[idx:idx+count] = [number]*count
        idx += count
    return array


if __name__ == '__main__':
    array = [1, 0, 0, -1, -1, 0, 1, 1]
    order = [0, 1, -1]
    print(threeNumberSort(array, order))
