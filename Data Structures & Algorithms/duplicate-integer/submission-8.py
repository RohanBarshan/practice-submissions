class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        bag = set()

        for n in nums:
            if n in bag:
                return True
            else:
                bag.add(n)
        return False