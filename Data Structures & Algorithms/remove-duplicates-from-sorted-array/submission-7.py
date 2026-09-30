class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        k = 0

        for num in nums:
            if num not in seen:
                seen.add(num)
                nums[k] = num
                k += 1
        return k