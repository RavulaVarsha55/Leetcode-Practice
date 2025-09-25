from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        countArray=Counter(arr)
        seen=[]
        for key,value in countArray.items():
            if value in seen:
                return False
            seen.append(value)
        return True
        