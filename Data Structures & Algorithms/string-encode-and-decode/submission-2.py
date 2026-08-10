class Solution:

    def encode(self, strs: List[str]) -> str:
        #"5#ROHAN 3#DEB"
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        # "5#ROHAN 3#DEB" - /decoding

        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            length = int(s[i : j])
            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return res
