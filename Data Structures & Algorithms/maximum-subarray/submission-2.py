class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # if sum is 0, set it to 0, if it isn't keep adding
        current_sum = -float("inf")
        max_sum = -float("inf")
        
        for num in nums:
            if current_sum < 0:
                current_sum = 0
            current_sum += num
            max_sum = max(max_sum, current_sum)
        
        return max_sum