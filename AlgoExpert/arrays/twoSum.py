def twoNumberSum(array, targetSum):  # O(n^2)  time | O(1) space
    # Write your code here.
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            suma = array[i] + array[j]
            if suma == targetSum:
                return [array[i], array[j]]
    return []


def twoNumberSum2(array, targetSum):  # O(n)  time | O(n) space
    hashmap = {}
    for value in array:
        potential_match = targetSum - value
        if potential_match in hashmap:
            return [potential_match, value]
        else:
            hashmap[value] = targetSum - value
    return []


if __name__ == "__main__":
    array = [3, 5, -4, 8, 11, 1, -1, 6]
    targetSum = 10
    print(twoNumberSum2(array, targetSum))
