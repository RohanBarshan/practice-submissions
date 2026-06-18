class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        rohan = set()

        for n in nums:
            if n in rohan:
                return True
            else:
                rohan.add(n)
        return False