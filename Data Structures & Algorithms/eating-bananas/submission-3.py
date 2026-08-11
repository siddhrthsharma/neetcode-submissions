import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        min_k = right


        while left <= right:
            curr_k = (left + right) // 2
            tot_hr = 0

            for pile in piles:
                tot_hr += math.ceil(pile/curr_k)

            if tot_hr <= h:
                min_k = min(min_k, curr_k)
                right = curr_k - 1
            else:
                left = curr_k + 1

        return min_k
