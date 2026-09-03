from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        asc_vals = defaultdict(list)

        for string in strs:
            output = [0] * 26
            for char in string:
                output[ord(char) - ord('a')] += 1
            
            asc_vals[tuple(output)].append(string)
        
        return list(asc_vals.values())