class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        

        def helper(i, nums, curSet, subSets):
            if i == len(nums):
                subSets.append(curSet.copy())
                return 



            curSet.append(nums[i])
            helper(i+1, nums, curSet, subSets)
            curSet.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            helper(i+1, nums, curSet, subSets)



        nums.sort()
        subSets = []
        curSet = []

        helper(0, nums, curSet, subSets)
        return subSets