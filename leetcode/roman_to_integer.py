class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        suma = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace(
            "XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
        for ch in reversed(s):
            suma += roman_values[ch]
        return suma


cases = ["III",
         "LVIII",
         "MCMXCIV"]

for case in cases:
    print(Solution().romanToInt(case))
