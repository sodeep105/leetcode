class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res, sol = [], []

        total = 0

        def dfs(i, total):
            if total == target:
                res.append(sol[:])
                return 
            
            if i == len(candidates) or total > target:
                return
            
            sol.append(candidates[i])
            dfs(i, total+candidates[i])
            sol.pop()

            dfs(i+1, total)
        
        dfs(0,0)
        return res