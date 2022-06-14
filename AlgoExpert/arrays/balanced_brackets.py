from collections import deque

from grpc import channel_ready_future


def balancedBrackets(string):
    # Write your code here.
    brackets = {
        "(": ")",
        "{": "}",
        "[": "]"
    }
    queue = deque()
    left_brackets = ["(", "[", "{"]
    right_brackets = [")", "]", "}"]
    for bracket in string:
        if bracket in left_brackets:
            queue.append(bracket)
        elif bracket in right_brackets:
            if len(queue) > 0:
                last_left = queue.pop()
                if bracket != brackets[last_left]:
                    return False
            else:
                return False
        else:
            continue
    return len(queue) == 0


def isValid(string):
    brackets = {
        "(": ")",
        "{": "}",
        "[": "]"
    }
    stack = []
    for ch in string:
        if brackets.get(ch):
            stack.append(ch)
        else:
            last_opened_bracket = stack.pop()
            if brackets[last_opened_bracket] != ch:
                return False
    return len(stack) == 0


if __name__ == "__main__":
    input_dict = {
        "string": "([])(){}(())()()"
    }
    print(isValid(input_dict["string"]))
