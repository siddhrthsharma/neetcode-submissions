class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []
        
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            
        freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))

        for key in freq:
            if k == 0:
                break
            res.append(key)
            k -= 1
        
        return res