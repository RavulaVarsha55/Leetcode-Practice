class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict=set()
        maxlen=0
        left=0 #tracks rightv 
        for right in range(len(s)):
            if s[right] not in dict:#start from s[0] is this is not in dict means new so add 

                dict.add(s[right])
                maxlen=max(maxlen,len(dict))
                print(maxlen)
                print(f"inside if{dict}")
            else:
                while s[right] in dict:
                    dict.remove(s[left])
                    left=left+1
                dict.add(s[right])
            
        
        return maxlen