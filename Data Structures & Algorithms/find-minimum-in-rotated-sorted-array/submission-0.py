class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums) - 1

        if nums[r] > nums[l]:
            return nums[0]
        
        while nums[r] < nums[l]:
            l += 1
        
        return nums[l]