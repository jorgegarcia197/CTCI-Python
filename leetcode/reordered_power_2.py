# You are given an integer n. We reorder the digits in any order (including the original order) such that the leading digit is not zero.
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        """You are given an integer n. We reorder the digits in any order (including the original order) such that the leading digit is not zero.
        Return true if and only if it is a power of 2.
        """
        s = str(n)
        return s == ''.join(sorted(s)) and s[0] != '0'