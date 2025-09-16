import random
class Solution:
    def sumZero(self, n: int) -> List[int]:
        ray=int(n/2)
        randArray=[]
        for i in range(1,ray+1):
            randArray.append(i)
            randArray.append(-i)

        if n%2==1:
            randArray.append(0)
        return randArray 