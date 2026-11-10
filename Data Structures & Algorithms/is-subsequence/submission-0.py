class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        
        j = 0

        for i in range(len(t)):
            if j < len(s) and t[i] == s[j]:
                j += 1
        
        return j == len(s)