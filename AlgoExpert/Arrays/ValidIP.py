def validIPAdresses(string: str):
    ip_found = []

    for i in range(1, min(len(string), 4)):
        # Check if the first segment is a valid IP
        currentIP_address_part = ["", "", "", ""]
        currentIP_address_part[0] = string[:i]  # Up until index i (inclusive)
        if not isValidPart(currentIP_address_part[0]):
            continue
        for j in range(i + 1, i + min(len(string)-i, 4)):
            currentIP_address_part[1] = string[i:j]
            if not isValidPart(currentIP_address_part[1]):
                continue
            for k in range(j + 1, j + min(len(string)-j, 4)):
                currentIP_address_part[2] = string[j:k]
                currentIP_address_part[3] = string[k:]
                if isValidPart(currentIP_address_part[2]) and isValidPart(currentIP_address_part[3]):
                    ip_found.append(".".join(currentIP_address_part))
    return ip_found

def isValidPart(string: str):
    stringAsInt = int(string)
    if stringAsInt > 255 or stringAsInt < 0:
        return False
    # This is done to check if the string is the same length as the integer to remove leading 0s
    return len(string) == len(str(stringAsInt))
