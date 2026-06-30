class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        rohan = set()
        L = 0
        res = 0

        for R in range(len(s)):
            while s[R] in rohan:
                rohan.remove(s[L])
                L += 1

            rohan.add(s[R])
            res = max(res, R - L + 1)
        return res