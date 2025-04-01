class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res, par = [], []
        def dfs(i):
            if i == len(s):
                res.append(par[:])
                return
            for j in range(i, len(s)):
                if self.is_palin(i,j,s):
                    par.append(s[i:j+1])
                    dfs(j+1)
                    par.pop()   

            return res
        
        dfs(0)
        return res

    def is_palin(self, l, r, s):
        while l<=r:
            if s[l] != s[r]:
                return False
            l = l+1
            r = r-1
        return True
                

        