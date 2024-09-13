class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j = 0,0
        ans = ""
        while i < len(s) and j <len(t):
            if s[i] == t[j]:
                j+=1
                i+=1
                
            else:
                j+=1

        return i == len(s)