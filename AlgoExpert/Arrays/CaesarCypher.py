import string


def cypher(input_string, key):
    alphabet = {}
    output = []
    new_key = key % 25
    for num, s in enumerate(string.ascii_lowercase):
        alphabet[ord(s)] = s
    for letter in input_string:
        num = ord(letter) + new_key
        if num > 122:
            num = num % 122
            output.append(alphabet[num+96])
        else:
            output.append(alphabet[num])
    return "".join(output)

def cypher2(input_string, key):
    alphabet = list(string.ascii_lowercase)
    output = []
    new_key = key % 25
    for s in input_string:
        output.append(alphabet[(alphabet.index(s) + new_key) % 26])
    return "".join(output)
    


if __name__ == "__main__":
    print(cypher2("xyz", 2))
