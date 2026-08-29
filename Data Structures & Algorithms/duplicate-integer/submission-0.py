class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupes = {}
        for num in nums:
            dupes[num] = dupes.get(num, 0) + 1
            if dupes[num] >= 2:
                return True
        return False