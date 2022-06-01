def isValidSubsequence(array, sequence):
    # Write your code here.
    found = 0
    for idx, value in enumerate(array):
        if value == sequence[0]:
            startingIdx = idx
            found += 1
            break
    if found == 0:
        return False
    elif startingIdx == 0:
        startingIdx = 1

    while startingIdx < len(array) and found < len(sequence):
        if array[startingIdx] == sequence[found]:
            found += 1
        startingIdx += 1

    return found == len(sequence)


if __name__ == "__main__":
    print(isValidSubsequence([1, 1, 6, 1], [1, 1, 1, 6]))
