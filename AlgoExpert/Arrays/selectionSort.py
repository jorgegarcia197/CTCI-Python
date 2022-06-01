def selectionSort(array):
    # Write your code here.
    output_array = []
    for i in range(len(array)):
        smallest = findSmallest(array)
        output_array.append(array.pop(smallest))
    return output_array


def findSmallest(array):
    smallest = array[0]
    small_idx = 0
    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            small_idx = i
    return small_idx


print(selectionSort([5, 3, 6, 2, 10]))
