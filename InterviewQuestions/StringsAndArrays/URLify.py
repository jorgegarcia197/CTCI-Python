def URLify(s: str, length: int):
    num_spaces = s.strip().count(' ')  # we get the count of the empty spaces
    s = list(s)  # we convert the string to a list
    # "The new index we can iterate through"
    new_index = length + (num_spaces * 2) - 1
    for i in range(length - 1, -0, -1):
        if s[i] == ' ':  # If we hit a space, we replace it with %20 and move the index back by 2 spaces
            s[new_index] = '0'
            s[new_index - 1] = '2'
            s[new_index - 2] = '%'
            new_index -= 3
        else:
            s[new_index] = s[i]
            new_index -= 1
    return ''.join(s)


if __name__ == '__main__':
    s = "Mr John Smith    "
    print(URLify(s, 13))
    # "Mr%20John%20Smith"
