class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        max_len = 0
        n = len(s)
        for i in range(len(s)):
            #odd length
            left,right = i,i
            while left>=0 and right<n and s[left] == s[right]:
                if right - left +1 > max_len:
                    res = s[left:right+1]
                    max_len = right - left +1
                left-=1
                right+=1
            #even length
            left,right = i,i+1
            while left>=0 and right<n and s[left] == s[right]:
                if right - left +1 > max_len:
                    res = s[left:right+1]
                    max_len = right - left +1
                left-=1
                right+=1
        return res
