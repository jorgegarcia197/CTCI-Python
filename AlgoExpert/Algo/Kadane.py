# Kadane's Algorithm

def kadane(array):
    max_sum = -float('inf')
    offset = 0
    for i in range(0, len(array)):
        subset = array[offset:i+1]
        total_sum = sum(array[offset:i+1])
        if total_sum < array[i]:
            offset = i
            total_sum = array[i]
        max_sum = max(max_sum, total_sum)
    return max_sum


if __name__ == "__main__":
    array = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
    print(kadane(array))
