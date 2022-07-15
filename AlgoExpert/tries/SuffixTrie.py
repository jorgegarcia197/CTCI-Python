class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        # Write your code here.
        for i in range(len(string)):
            self.insert(i, string)

    def insert(self, idx, string):
        node = self.root
        for inner in range(idx, len(string)):
            letter = string[inner]
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node[self.endSymbol] = True

    def contains(self, string):
        # Write your code here.
        for i in range(len(string)):
            contained =self.lookup(i, string)
            
            
    def lookup(self, idx, string):
        node = self.root
        for inner in range(idx, len(string)):
            letter = string[inner]
            if letter not in node:
                return False
            node = node[letter]
        return self.endSymbol in node

