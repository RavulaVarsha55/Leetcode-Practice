class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        ltext=text.split(" ")
        count=0
        for i in ltext:
            flag=1
            for c in i:
                if c in brokenLetters:
                    
                    flag=0
                    count=count+1
                    break
        return len(ltext)-count