class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # keep track of the current word and when we find a diff one, add to it.
        # perform a substitution once in each run (# of subs depends on k)
        # we could do a loop to substitute letters not in the set

        count = {}
        res = 0             
        maxf = 0
        l = 0
        r = 0

        for r in range(len(s)):
            count[s[r]]= 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
             
        return res
        print(count)
    