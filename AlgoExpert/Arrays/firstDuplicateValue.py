def firstDuplicateValue(array):
    # Write your code here.
    hashmap = {}
    for idx, value in enumerate(array):
        if value not in hashmap:
            hashmap[value] = idx
        else:
            return value
    return []


if __name__ == "__main__":
    array = [2, 1, 5, 3, 3, 2, 4]
    print(firstDuplicateValue(array))
