from itertools import count
from turtle import left


string = "AlgoExpert is the best!"


def create_words_array(string):
    if string == "":
        return ""
    left = 0
    right = 0
    length = len(string)
    whitespaces = []
    words = []
    space = " "
    while left < length or right < length:
        if string[left] != space:
            word = []
            while right < length and string[right] != space:
                word.append(string[right])
                right += 1
            words.append("".join(word))
            left = right
            right = left + 1
        else:
            spaces = []
            spaces.append(string[left])
            while right < length and string[right] == space:
                spaces.append(string[right])
                right += 1
            whitespaces.append("".join(spaces))
            left = right
            right = left
    c = []
    words, whitespaces = words[::-1], whitespaces[::-1]
    for i in range(min(len(words), len(whitespaces))):
        c.append(words[i])
        c.append(whitespaces[i])
    if len(words) > len(whitespaces):
        c.extend(words[i+1:])
    else:
        c.extend(whitespaces[i+1:])
    return c


def reverseWordsInString(string):
    # Write your code here.
    words = []
    start = 0
    for idx, char in enumerate(string):
        if char == " ":
            words.append(string[start:idx])
            start = idx
        elif string[start] == " ":
            words.append(" ")
            start = idx
    words.append(string[start:]).reverse()
    return "".join(words)


if __name__ == "__main__":
    words = reverseWordsInString(string)
    print(words)
