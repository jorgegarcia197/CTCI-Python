from collections import deque, Counter


def find_averages_of_subarrays(k, array):
    result = []
    window = deque()
    window.extend(array[:k])
    for i in range(k, len(array)):
        total_window = sum(window)
        result.append(total_window/k)
        window.append(array[i])
        window.popleft()
    total_window = sum(window)
    result.append(total_window/k)
    return result


def max_sub_array_of_size_k(k, arr):
    result = []
    window = deque()
    window.extend(arr[:k])
    max_sum = sum(window)
    for i in range(k, len(arr)):
        total_window = sum(window)
        if total_window > max_sum:
            max_sum = total_window
            result = window.copy()
        window.append(arr[i])
        window.popleft()
    return list(result)


def min_sub_array(target, array):
    window_start = 0
    window_end = 0
    min_length = float("inf")
    while window_end < len(array)+1:
        window = array[window_start:window_end]
        if sum(window) >= target:
            min_length = min(min_length, window_end - window_start)
            window_start += 1
        else:
            window_end += 1
    return min_length


def longest_string_without_repeating(str1, k):
    window_start = 0
    max_length = 0
    frequency_hash = {}
    for window_end in range(len(str1)):
        right = str1[window_end]
        if right not in frequency_hash:
            frequency_hash[right] = 0
        frequency_hash[right] += 1

    # shrink the sliding window, until we are left with 'k' distinct characters in the frequency_hash
        while len(frequency_hash) > k:
            left_char = str1[window_start]
            frequency_hash[left_char] -= 1
            if frequency_hash[left_char] == 0:
                del frequency_hash[left_char]
            window_start += 1  # shrink the window
        # remember the maximum length so far
        max_length = max(max_length, window_end-window_start + 1)
    return max_length


def longest_substring_with_k_distinct(str1, k):
    window_start = 0
    max_length = 0
    char_frequency = {}

    # in the following loop we'll try to extend the range [window_start, window_end]
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1

        # shrink the sliding window, until we are left with 'k' distinct characters in the char_frequency
        while len(char_frequency) > k:
            left_char = str1[window_start]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            window_start += 1  # shrink the window
        # remember the maximum length so far
        max_length = max(max_length, window_end-window_start + 1)
    return max_length


if __name__ == "__main__":
    print(longest_string_without_repeating("araaci",  2))
    print(longest_string_without_repeating("araaci",  1))
    print(longest_string_without_repeating("cbbebi", 3))
    print(longest_string_without_repeating("cbbebi", 10))
