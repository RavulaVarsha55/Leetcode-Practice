class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowelMap={'a':0,'e':0,'i':0,'o':0,'u':0}
        consMap={}
        maxV,maxC=0,0;
        for i in s:
            if i in vowelMap:
                vowelMap[i]=vowelMap[i]+1;
                maxV=max(maxV,vowelMap[i])
            else:
                if i in consMap:
                    consMap[i]=consMap[i]+1;
                    maxC=max(maxC,consMap[i])
                else:
                    consMap[i]=1;
                    maxC=max(maxC,consMap[i])
    
        return maxC+maxV;