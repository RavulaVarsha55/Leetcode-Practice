from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            sMap=Counter(s)
            tMap= Counter(t)
            return sMap==tMap
        return False

        