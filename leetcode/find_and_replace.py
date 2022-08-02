#! https://leetcode.com/problems/find-and-replace-pattern/
from typing import List
from collections import Counter
"""Given a list of strings words and a string pattern, return a list of words[i] that match pattern. You may return the answer in any order.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.

Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation, since a and b map to the same letter.
"""


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        pattern_counter = Counter(pattern)
        words_pattern = []
        for word in words:
            word_pattern = Counter(word)
            values_counter = list(pattern_counter.values())
            word_values = list(word_pattern.values())
            if values_counter == word_values:
                words_pattern.append(word)
        return words_pattern

    def findAndReplacePattern_2(self, words: List[str], pattern: str) -> List[str]:
        def match(w1: str, w2: str) -> bool:
            if len(w1) != len(w2):
                return False
            mp1, mp2 = {}, {}
            for a, b in zip(w1, w2):
                mp1[a] = b
                mp2[b] = a
            for a, b in zip(w1, w2):
                if mp1[a] != b or mp2[b] != a:
                    return False
            return True
        return [w for w in words if match(w, pattern)]


if __name__ == "__main__":
    words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
    pattern = "abb"
    print(Solution().findAndReplacePattern_2(words, pattern))
