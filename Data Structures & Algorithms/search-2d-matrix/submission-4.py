class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        top_row = 0
        bottom_row = rows - 1

        while top_row <= bottom_row:
            curr_row = (top_row + bottom_row) // 2

            if target >= matrix[curr_row][0] and target <= matrix[curr_row][-1]:
                break

            if target > matrix[curr_row][-1]:
                top_row = curr_row + 1
            elif target < matrix[curr_row][0]:
                bottom_row = curr_row - 1 
            
        left = 0
        right = len(matrix[curr_row]) - 1

        while left <= right:
            mid = (left + right) // 2

            if target == matrix[curr_row][mid]:
                return True

            elif target > matrix[curr_row][mid]:
                left = mid + 1

            else:
                right = mid - 1
        
        return False

            

