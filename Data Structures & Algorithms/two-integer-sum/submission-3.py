class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}

        for i, num in enumerate(nums):
            if target - num in freq:
                return [freq[target-num], i]
            freq[num] = i