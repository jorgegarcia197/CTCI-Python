import math

input_str = "abaxyzzyxf"


def isOdd(length: int) -> bool:
    if length % 2 == 1:
        return True
    else:
        return False


def isPalindrome(string):
    # converting the string as an array to iterate thru
    string = string.lower().strip()
    string = list(string)
    if len(string) <= 1:
        return True

    length = len(string)
    if isOdd(length):
        mid = (math.ceil(length/2))-1
        left = mid
        right = mid
    else:
        mid = (length//2)-1
        left = mid
        right = mid + 1

    while left >= 0 and right <= length:
        if string[left] != string[right]:
            return False
        left -= 1
        right += 1

    # Write your code here.
    return True


def getLongestPalindromeFrom(string, left, right):
    while left >= 0 and right < len(string):
        if string[left] != string[right]:
            break
        left -= 1
        right += 1
    return [left+1, right]


def longestPalindromicSubstring(string):
    # Write your code here.
    longest_palindrome = [0, 1]
    for i in range(1, len(string)):
        odd = getLongestPalindromeFrom(string, i-1, i+1)
        even = getLongestPalindromeFrom(string, i-1, i)
        longest = max(odd, even, key=lambda x: x[1]-x[0])
        longest_palindrome = max(
            longest_palindrome, longest, key=lambda x: x[1]-x[0])
    return string[longest_palindrome[0]:longest_palindrome[1]]


if __name__ == "__main__":

    input_str = "abaxyzzyxf"
    print(longestPalindromicSubstring(input_str))
