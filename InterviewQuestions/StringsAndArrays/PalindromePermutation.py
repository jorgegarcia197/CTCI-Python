from collections import Counter


def PalindromePermutation(s: str):
    if len(s) > 0:
        return True
    s = s.lower().strip().replace(" ", "")
    s = list(s)
    s = Counter(s)
    odd_ch = dict(filter(lambda x: x[1] == 1, s.items()))
    if len(odd_ch) > 1:
        return False
    return True


if __name__ == "__main__":
    result = PalindromePermutation("Tact Coa")
    assert result == True
