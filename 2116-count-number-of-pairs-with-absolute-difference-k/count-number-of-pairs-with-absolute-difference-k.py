from collections import Counter
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count=0
        count_nums=Counter(nums)
        for i in nums:
            if (i-k) or (i+k) in nums:
                count=count+count_nums[i-k]
        return count