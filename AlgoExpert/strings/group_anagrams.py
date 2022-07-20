

def group_anagrams(words):
    hash_map = {}
    for word in words:
        sorted_letters = ''.join(sorted(word))
        if sorted_letters not in hash_map:
            hash_map[sorted_letters] = [word]
        else:
            hash_map[sorted_letters].append(word)
    
    return list(hash_map.values())

if __name__ == "__main__":
    words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
    print(group_anagrams(words))
    