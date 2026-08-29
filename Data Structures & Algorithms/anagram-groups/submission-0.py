class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_group = {}

        for words in strs:
            key = ''.join(sorted(words))
            if key not in word_group:
                word_group[key] = [] # initialize the array w/ the key
            word_group[key].append(words) # use the sorted key and append whichever value matches
        
        return list(word_group.values())
