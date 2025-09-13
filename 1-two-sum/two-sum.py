class Solution:
    #twosum
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        keysDict = {}
        for i in range(len(nums)):
            num = nums[i]
            remSum = target - num
            if remSum in keysDict:
                return [keysDict[remSum], i]
            keysDict[num] = i
        return []
