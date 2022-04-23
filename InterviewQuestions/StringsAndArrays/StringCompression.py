

def stringCompression(s: str):
    if len(s) < 0:
        return s
    count = 0
    length = len(s) - 1
    s = list(s.lower().strip().replace(" ", ""))
    left = right = 0
    output = []
    while left <= length:
        if right <= length and s[right] == s[left]:
            # if the left and right are the same, increment the count and advance the pointer
            count += 1
            right += 1
        else:
            # Advance left to the right, reset the counter to 0 and append the character and count to the output
            output.append(s[left])
            output.append(str(count))
            count = 0
            left = right
    output = "".join(output)
    if len(output) > len(s):
        return s
    return output


if __name__ == "__main__":
    s = "aabcccccaaa"
    output = stringCompression(s)
    assert output == "a2b1c5a3"
