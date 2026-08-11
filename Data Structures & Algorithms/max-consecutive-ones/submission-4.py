class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes = res = 0

        for n in nums:
            if n == 1:
                maxOnes += 1
                res = max(res, maxOnes)
            
            else:
                maxOnes = 0
        
        return res
        
        