
import math
# Having a list of integers, return the sum of all the products of every index excluding the indext itself

input_list = [2, 3, 4, 5]
sample_output = [60, 40, 30, 24]


def sum_excluding(List):
    output = []
    for idx, value in enumerate(List):
        output.append(get_left(List, idx)*get_right(List, idx))
    return output


def get_left(list, idx):
    return math.prod(list[:idx])


def get_right(list, idx):
    return math.prod(list[idx+1:])


def product_exclusion(nums):
    left = [1]
    right = [1]
    for i in range(1, len(nums)):
        left.append(left[i-1]*nums[i-1])

    for num in reversed(nums[1:]):
        right.append(right[-1]*num)
    right = right[::-1]
    for i in range(len(nums)):
        nums[i] = left[i]*right[i]

    return nums


if __name__ == "__main__":
    output = product_exclusion(input_list)
    print(output)
