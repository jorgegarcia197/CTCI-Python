

from cgi import test
from collections import Counter


def isUnique(s: str):
    # return True if all characters in string are unique
    s = s.lower().strip().replace(" ", "")
    seen = {}
    for index, ch in enumerate(s):
        if ch not in seen:
            seen[ch] = index
        else:
            return False
    return True


if __name__ == '__main__':
    test1 = isUnique('abcdefghijklmnopqrstuvwxyz')
    assert test1 == True
    test2 = isUnique("aba")
    assert test2 == False
    test3 = isUnique("How are you doing")
    assert test3 == False
    test4 = isUnique("car")
    assert test4 == True
