class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res, cur = [], []

        def backtracking(i): 
            if len(cur) == k:
                res.append(cur[:])
                return
            
            for j in range(i,n+1):
                cur.append(j)
                backtracking(j+1)
                cur.pop()

        backtracking(1)
        return res            