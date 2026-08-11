class Solution:
    def binarySearch(self, nums: List[int], target) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            elif target > nums[mid]:
                left = mid + 1

            else:
                right = mid - 1
            
        return -1

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # check which row
        # if target is less than the first element of the current row
        # then go to the previous row (cut in half, everything in front)
        # decrement right pointer
        # if target is greater " "
        # then to go the next row (cut in half, everything behind)
        # increment left pointer
        left = 0
        right = len(matrix) - 1

        while left <= right:
            mid = (left + right) // 2 

            if self.binarySearch(matrix[mid], target) >= 0:
                return True

            if target > matrix[mid][0]:
                left = left + 1
            
            else:
                right = right - 1
        
        return False