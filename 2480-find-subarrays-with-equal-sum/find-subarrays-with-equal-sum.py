class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        seen=[]
        for i in range(len(nums)-1):
            if nums[i]+nums[i+1] in seen:
                return True
            seen.append(nums[i]+nums[i+1])
        return False
        