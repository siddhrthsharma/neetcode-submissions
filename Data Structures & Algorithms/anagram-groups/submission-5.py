class Solution:
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #   word_group = {}

    #   for words in strs:
    #      key = ''.join(sorted(words))
    #      if key not in word_group:
    #          word_group[key] = [] 
    #      word_group[key].append(words) # use the sorted key and append whichever value matches
        
    #   return list(word_group.values())

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letter_group = defaultdict(list)

        for word in strs:
            count = [0] * 26 
            for char in word:
                count[ord(char) - ord('a')] += 1

            letter_group[tuple(count)].append(word)
        
        return list(letter_group.values())
            