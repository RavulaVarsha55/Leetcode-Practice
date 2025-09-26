from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freqCounter= Counter(nums)
        for i,count in freqCounter.items():
            if(count<2):
                return i


        