class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        k = 0
        for n in nums:
            if val != n:
                nums[k] = n

                k += 1
        return k