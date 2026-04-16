class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=0
        for i in nums:
            res=res^i
        return res
    # xor gives if two bits are same zero otherise false
    # xor with same number gives zero
    # xor with zero gives org num which is what we wan
    # xor provides associative and commutatuive so felixibility of order
    
        
        