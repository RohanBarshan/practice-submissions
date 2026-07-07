class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for n in nums:
            nextPerm = []
            for p in perms:
                for i in range(len(p) + 1):
                    pCopy = p.copy()
                    pCopy.insert(i, n)
                    if pCopy not in nextPerm:
                        nextPerm.append(pCopy)
                perms = nextPerm
        return perms