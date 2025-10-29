class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def issorted(a):
            return all(a[i] <= a[i + 1] for i in range(len(a) - 1))
        operations=0
        while not issorted(nums):
            pairs = [x+y for x, y in pairwise(nums)]
            i = pairs.index(m := min(pairs))
            nums[i] = m
            nums.pop(i+1)
           # select i and i+1 in such a way their sum is min
            
            #add back to array
            
            operations+=1
        return operations