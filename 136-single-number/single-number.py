from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c=Counter(nums)
        return [i for i in c.keys() if c[i]<2][0]
        