from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cntr, w, match = Counter(s1), len(s1), 0

        for i in range(len(s2)):
            if s2[i] in cntr:
                if not cntr[s2[i]]:
                    match -= 1
                cntr[s2[i]] -= 1
                if not cntr[s2[i]]:
                    match += 1

            if i >= w and s2[i-w] in cntr:
                if not cntr[s2[i-w]]:
                    match -= 1
                cntr[s2[i-w]] += 1
                if not cntr[s2[i-w]]:
                    match += 1

            if match == len(cntr):
                return True

        return False


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r, w_size = 0, 0, len(s1)

        while r < len(s2):
            if r - l + 1 < w_size:
                r += 1
            elif Counter(s2[l:r+1]) == Counter(s1):
                return True
            else:
                l += 1
                r += 1

        return False


s1 = "ab"
s2 = "eidbaooo"
print(Solution().checkInclusion(s1, s2))
