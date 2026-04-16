class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res=len(nums)
        return (res*res + res)//2-(sum(nums))
        