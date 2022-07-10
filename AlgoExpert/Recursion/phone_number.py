

number_mappings = {
    "1": "1",
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
    "0": "0"
}


def phoneNumberMnemonics(phoneNumber):
    result = []
    current = ["0"] * len(phoneNumber)

    return pick_char(0, current, phoneNumber, result)


def pick_char(idx, current, phoneNumber, result):
    if idx >= len(phoneNumber):
        result.append("".join(current))
        return
    for char in number_mappings[phoneNumber[idx]]:
        current[idx] = char
        pick_char(idx+1, current, phoneNumber, result)
    return result


if __name__ == "__main__":
    input_str = "1905"
    print(phoneNumberMnemonics(input_str))
