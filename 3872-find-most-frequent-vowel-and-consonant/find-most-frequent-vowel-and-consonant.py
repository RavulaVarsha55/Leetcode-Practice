class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels={'a','e','i','o','u'}
        vowelMap={}
        consMap={}
        maxV=0;
        maxC=0;
        for i in s:
            print(i)
            if i in vowels:
                if i in vowelMap:
                    vowelMap[i]=vowelMap[i]+1;
                    if(maxV<vowelMap[i]): 
                        maxV=vowelMap[i]
                else:
                    vowelMap[i]=1;
                    maxV=max(maxV,vowelMap[i])

            else:
                if i in consMap:
                    consMap[i]=consMap[i]+1;
                    if(maxC<consMap[i]): 
                        maxC=consMap[i]
                else:
                    consMap[i]=1;
                    maxC=max(maxC,consMap[i])
    
        return maxC+maxV;