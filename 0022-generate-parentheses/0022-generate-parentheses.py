class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        stack, res = [], []

        def dfs(openC, closeC):
            if openC == closeC == n:
                res.append("".join(stack))

            if openC < n:
                stack.append('(')
                dfs(openC+1, closeC)
                stack.pop()
            
            if closeC < openC:
                stack.append(')')
                dfs(openC,closeC+1)
                stack.pop()
        dfs(0,0)
        return res         