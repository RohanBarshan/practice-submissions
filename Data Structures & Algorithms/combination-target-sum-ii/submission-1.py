class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, subset, total):
            if total == target:
                res.append(subset.copy())
                return 
            
            if i >= len(candidates) or total > target:
                return
            
            #includes candidates
            subset.append(candidates[i])
            dfs(i + 1, subset, total + candidates[i])
            subset.pop()

            #not include candidates
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, subset, total)
        dfs(0, [], 0)
        return res