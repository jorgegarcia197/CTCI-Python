
from min_heap import MinHeap


def sortKSortedArray(array, k):
    # Write your code here.
    minheap_with_k_elements = MinHeap(array[:min(k+1, len(array))])
    next_index = 0
    for idx in range(k+1, len(array)):
        minElement = minheap_with_k_elements.remove()
        array[next_index] = minElement
        next_index += 1
        current_element = array[idx]
        minheap_with_k_elements.insert(current_element)
    while not minheap_with_k_elements.is_empty():
        minElement = minheap_with_k_elements.remove()
        array[next_index] = minElement
        next_index += 1
    return array
