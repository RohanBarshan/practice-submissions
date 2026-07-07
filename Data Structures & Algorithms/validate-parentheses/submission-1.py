class Solution:
    def isValid(self, s: str) -> bool:
        rohan = []
        closeToOpen = {")":"(", "}":"{", "]":"["}

        for c in s:
            if c in closeToOpen:
                if rohan and rohan[-1] == closeToOpen[c]:
                    rohan.pop()
                else:
                    return False
            else:
                rohan.append(c)
        return True if not rohan else False