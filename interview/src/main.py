# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

# VALID: (){}[](()) VALID: ()
# INVALID: (() INVALID: {}((})

# Return True | False


hash_map = {
    "(": ")",
    "{": "}",
    "[": "]"
}


def isValid(s: str):
    s = list(s)
    stack = []
    for ch in s:
        # O(N) -> replacing right_brackets list and hash_map.keys()
        if hash_map.get(ch):
            stack.append(ch)
        else:
            last_opened_bracket = stack.pop()
            if hash_map[last_opened_bracket] != ch:
                return False
    return len(stack) == 0


if __name__ == "__main__":
    s = "((("
    print(isValid(s))
