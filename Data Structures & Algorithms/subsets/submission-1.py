class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        

        def helper(i, nums, curSet, subSets):
            if i >= len(nums):
                subSets.append(curSet.copy())
                return 


            curSet.append(nums[i])
            helper(i+1, nums, curSet, subSets)
            curSet.pop()

            helper(i+1, nums, curSet, subSets)

        subSets = []
        curSet = []
        helper(0, nums, curSet, subSets)
        return subSets