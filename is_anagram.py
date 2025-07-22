class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = {}
        hash_t = {}
        for i in s:
            if i not in hash_s:
                hash_s[i] = 1
            else:
                hash_s[i] = hash_s[i]+1
        for j in t:
            if j not in hash_t:
                hash_t[j] = 1
            else:
                hash_t[j] = hash_t[j]+1
        if hash_s == hash_t:
            return True
        else:
            return False
