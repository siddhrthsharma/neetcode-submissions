class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = {}
        freq2 = {}
        for char in s:
            freq1[char] = freq1.get(char, 0) + 1

        for char in t:
            freq2[char] = freq2.get(char, 0) + 1

        are_identical = freq1 == freq2
        
        return are_identical