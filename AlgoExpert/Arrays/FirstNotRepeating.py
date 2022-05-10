from collections import Counter


def firstNonRepeatingCharacter(string):
    # Write your code here.
    counter = Counter(string)
    for s in string:
        if counter[s] == 1:
            return string.index(s)
    return -1


if __name__ == "__main__":
    print(firstNonRepeatingCharacter("abcdcaf"))
