

from sklearn.linear_model import PassiveAggressiveClassifier


def max_sum_adjacent(array):
    max_sum_odd = 0
    max_sum_even = 0
    for idx, value in enumerate(array):
        if idx % 2 == 0:
            max_sum_even = max(max_sum_even + value, max_sum_even)
        else:
            max_sum_odd = max(max_sum_odd+value, max_sum_odd)
    return max(max_sum_odd, max_sum_even)


if __name__ == "__main__":
    input_array = [75, 105, 120, 75, 90, 135]
    print(max_sum_adjacent(input_array))
