def powerset(array):
    # Write your code here.
    if not array:
        return [[]]
    elif len(array) == 1:
        return [array, []]
    else:
        value = [[array[0]] + x for x in powerset(array[1:])]
        return powerset(array[1:]) + value


if __name__ == "__main__":
    input_array = [1, 2, 3]
    print(powerset(input_array))
