from collections import Counter
def minimumCharactersForWords(words):
    # Write your code here.
    total_counters = {}
    output = []
    for word in words:
        letter_count = Counter(word)
        for k,v in letter_count.items():
            if k not in total_counters:
                total_counters[k] = v
            else:
                total_counters[k] = max(total_counters[k], v)
    for k,v in total_counters.items():
        output.extend([k] * v)
    
    return output



if __name__ == "__main__":
    words=  ["this", "that", "did", "deed", "them!", "a"]
    print(minimumCharactersForWords(words))