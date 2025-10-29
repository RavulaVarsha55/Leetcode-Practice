from collections import Counter
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnum=Counter(nums)
        del cnum[0]
        return len(cnum)

        