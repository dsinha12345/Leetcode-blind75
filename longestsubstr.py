class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        d= set()
        start, end = 0,0
        max_len = 0

        while end<len(s):
            while s[end] in d:
                d.remove(s[start])
                start+=1
            d.add(s[end])
            end+=1
            max_len = max(max_len, end-start)
        return max_len    
            
            
