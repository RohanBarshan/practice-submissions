class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapSt = {}
        mapTs = {}

        for i in range(len(s)):
            c1, c2 = s[i], t[i]

            if (c1 in mapSt and mapSt[c1] != c2) or (c2 in mapTs and mapTs[c2] != c1):
                return False
            mapSt[c1] = c2
            mapTs[c2] = c1
        return True