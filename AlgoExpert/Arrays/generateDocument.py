from collections import Counter

input_str = "Bste!hetsi ogEAxpelrt x "


def generateDocument(character, document):
    character_counter = Counter(character)
    document_counter = Counter(document)
    for key, value in document_counter.items():
        if key not in character_counter:
            return False
        if character_counter[key] < value:
            return False
    return True


if __name__ == "__main__":
    document = "AlgoExpert is the Best!"
    print(generateDocument(input_str, document))
