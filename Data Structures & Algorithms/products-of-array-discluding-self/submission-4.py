class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        
        # compute prefix
        i = 1
        prefix = 1
        while i < len(nums):
            output[0] = 1
                
            prefix *= nums[i-1]
    
            output[i] = prefix

            i += 1
        
        # compute postfix
        i = len(nums) - 1
        postfix = 1
        while i >= 0:
            output[i] *= postfix

            postfix *= nums[i]           

            i -= 1

        return output