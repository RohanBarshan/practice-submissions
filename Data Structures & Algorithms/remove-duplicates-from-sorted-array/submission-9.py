class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        seen = set()
        k = 0

        for n in nums:
            if n not in seen:
                seen.add(n)

                nums[k] = n
                k += 1
        return k
#        l = 1

#        for r in range(1, len(nums)):
 #           if nums[r] != nums[r-1]:
  #              nums[l] = nums[r]
  #              l += 1
   #     return l
   



