class Solution:
    def isValid(self, s: str) -> bool:
        dict1 = {"}":"{",")":"(","]":"["}
        stack = []
        for char in s:
            if char in "{[(":
                stack.append(char)
            else:
                if not stack:
                    return False
                if dict1[char] == stack.pop():
                    continue
                else:
                    return False
        if not stack:
            return True
        return False
            
            
