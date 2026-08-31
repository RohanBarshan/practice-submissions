class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS = Counter(s)
        countT = Counter(t)

        for letters in countS:
            if countS[letters] != countT.get(letters, 0):
                return False
        return True 