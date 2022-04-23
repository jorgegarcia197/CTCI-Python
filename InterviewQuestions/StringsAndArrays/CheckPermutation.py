from collections import Counter


def check_permutation(s1: str, s2: str):
    if len(s1) != len(s2):
        return False
    s1 = s1.lower().strip().replace(" ", "")
    s2 = s2.lower().strip().replace(" ", "")
    s1 = Counter(s1)
    s2 = Counter(s2)
    if s1 == s2:
        return True
    return False
