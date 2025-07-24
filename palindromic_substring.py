class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count=0

        i = 0
        while i<n:
            #odd occurences
            left,right = i,i
            while left>=0 and right<n and s[left]==s[right]:
                count+=1
                left-=1
                right+=1
            #even occurances
            left,right = i,i+1
            while left>=0 and right<n and s[left]==s[right]:
                count+=1
                left-=1
                right+=1
            i+=1
        
        return count
