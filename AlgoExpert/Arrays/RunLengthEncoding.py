from cgi import print_arguments


def RunLengthEncoding(s: str):
    if len(s) < 0:
        return s
    count = 0
    length = len(s) - 1
    s = list(s)
    left = right = 0
    output = []
    while left <= length:
        if right <= length and s[right] == s[left] and count < 9:
            # if the left and right are the same, increment the count and advance the pointer
            count += 1
            right += 1
        else:
            # Advance left to the right, reset the counter to 0 and append the character and count to the output
            output.append(str(count))
            output.append(s[left])
            
            count = 0
            left = right
    output = "".join(output)
    if len(output) > len(s):
        return s
    return output


if __name__ == "__main__":
    s = "************^^^^^^^$$$$$$%%%%%%%!!!!!!AAAAAAAAAAAAAAAAAAAA"
    output = RunLengthEncoding(s)
    print(output)
