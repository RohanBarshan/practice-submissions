class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element = {}

        for n in nums:
            element[n] = 1 + element.get(n,0)

            if element[n] > len(nums) / 2:
                return n