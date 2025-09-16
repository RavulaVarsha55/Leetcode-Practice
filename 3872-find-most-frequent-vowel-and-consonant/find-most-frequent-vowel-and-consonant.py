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
                    print(f"inside vowelmap",{i})
                    print(f" vowel  max",{maxV})
                    vowelMap[i]=vowelMap[i]+1;
                    if(maxV<vowelMap[i]): 
                        print(f"inside max vowelmap",{i})
                        maxV=vowelMap[i]
                else:
                    vowelMap[i]=1;
                    maxV=max(maxV,vowelMap[i])

            else:
                if i in consMap:
                    print(f"inside cowelmap",{i})
                    print(f" cons  max",{maxC})
                    print(f" current  cons map",{consMap[i]})
                    consMap[i]=consMap[i]+1;
                    if(maxC<consMap[i]): 
                        print(f"inside max cowelmap",{i})
                        maxC=consMap[i]
                        print(f'max C',{maxC})
                else:
                    consMap[i]=1;
                    maxC=max(maxC,consMap[i])
    
        return maxC+maxV;