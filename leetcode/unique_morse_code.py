from typing import List
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        transformations = set()
        letters = [chr(i) for i in range(97, 123)]
        morse_dict = dict(zip(letters, morse_code))
        for ch in words:
            ch = "".join([morse_dict[chr] for chr in ch])
            transformations.add(ch)
        return len(transformations)