from typing import List


class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        output = []
        for word in words:
            reversed_word = self.reverseString(list(word))
            output.append(reversed_word)
        return " ".join(output)

    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s)-1
        while left <= right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return "".join(s)


if __name__ == "__main__":
    input_words = "Let's take LeetCode contest"
    print(Solution().reverseWords(input_words))
