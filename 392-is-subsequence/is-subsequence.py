class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l,r=0,0
        if len(s)!=0:
            while r<len(t):
                if s[l]==t[r]:
                    if l==len(s)-1:
                        return True
                    l+=1
                r+=1
            return False
        else:
            return True
        
